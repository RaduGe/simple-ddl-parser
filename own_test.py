from simple_ddl_parser import DDLParser

# extra
import json
import pprint

parse_results = DDLParser("""create table test(
        data_sync_id bigint not null,
        sync_count bigint not null,
        sync_mark timestamp  not  null,
        sync_start timestamp  not null,
        sync_end timestamp  not null,
        message varchar(2000) null,
        primary key (data_sync_id, sync_start));


        ALTER TABLE grades ADD CONSTRAINT fk_grade_id FOREIGN KEY (grade_id) REFERENCES test(data_sync_id);""").run()

# changed this
#print(parse_results)

pprint.pprint(parse_results)