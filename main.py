import pm4py
from datetime import date


from pm4py.streaming.stream.live_event_stream import LiveEventStream
from pm4py.streaming.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualizer

live_event_stream = LiveEventStream()

streaming_dfg = dfg_discovery.apply()
live_event_stream.register(streaming_dfg)
live_event_stream.start()


log = pm4py.read_xes('../streaming_process_mining/files/input/bottom.xes')

static_event_stream = pm4py.convert_to_event_stream(log)
for event in static_event_stream:
    live_event_stream.append(event)

live_event_stream.stop()

#result
dfg, activities, start_activities, end_activities = streaming_dfg.get()

#save results
gviz = dfg_visualizer.apply(dfg, parameters={"start_activities": start_activities, "end_activities": end_activities, "format": "svg"})
dfg_visualizer.save(gviz, '../streaming_process_mining/files/dfg_' + str(date.today()) + '.svg')




