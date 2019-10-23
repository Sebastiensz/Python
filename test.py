object_point_lyr.edit_features(adds = [feat])
query_result1 = object_point_lyr.query(where='OBJECTID={0}'.format(1+frame_count//10))
object_point_lyr.attachments.add(query_result1.features[0].attributes['OBJECTID'],'C:\\path\\fissures_detectees.jpg')
