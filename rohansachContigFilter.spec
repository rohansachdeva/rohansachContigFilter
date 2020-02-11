/*
A KBase module: ContigFilter
This sample module contains one small method that filters contigs.
*/


module rohansachContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        Example app which filters contigs in an assembly using both a minimum contig length
    */
    funcdef run_rohansachContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        New app which filters contigs in an assembly using both a minimum and a maximum contig length
    */
    funcdef run_rohansachContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
