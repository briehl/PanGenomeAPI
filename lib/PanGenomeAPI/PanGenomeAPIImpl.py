# -*- coding: utf-8 -*-
#BEGIN_HEADER
from PanGenomeAPI.PanGenomeIndexer import PanGenomeIndexer
import os
#END_HEADER


class PanGenomeAPI:
    '''
    Module Name:
    PanGenomeAPI

    Module Description:
    A KBase module: PanGenomeAPI
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.1.0"
    GIT_URL = "https://github.com/kbaseapps/PanGenomeAPI.git"
    GIT_COMMIT_HASH = "6aa52d10d28fc46e3762cfc6df34be20ae8deef6"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.indexer = PanGenomeIndexer(config)
        #END_CONSTRUCTOR
        pass


    def search_orthologs_from_pangenome(self, ctx, params):
        """
        :param params: instance of type "SearchOrthologsFromPG" (num_found -
           optional field which when set informs that there is no need to
           perform full scan in order to count this value because it was
           already done before; please don't set this value with 0 or any
           guessed number if you didn't get right value previously.) ->
           structure: parameter "pangenome_ref" of String, parameter "query"
           of String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchOrthologsFromPGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "orthologs" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "orthologs" of list
           of type "OrthologsData" (OrthologFamily object: this object holds
           all data for a single ortholog family in a metagenome @optional
           type function md5 protein_translation) -> structure: parameter
           "id" of String, parameter "type" of String, parameter "function"
           of String, parameter "md5" of String, parameter
           "protein_translation" of String, parameter "orthologs" of list of
           tuple of size 3: String, Double, String, parameter "num_found" of
           Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_orthologs_from_pangenome
        result = self.indexer.search_orthologs_from_pangenome(ctx["token"],
                                                              params.get("pangenome_ref", None),
                                                              params.get("query", None),
                                                              params.get("sort_by", None),
                                                              params.get("start", None),
                                                              params.get("limit", None),
                                                              params.get("num_found", None))
        #END search_orthologs_from_pangenome

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_orthologs_from_pangenome return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def search_families_from_comparison_genome(self, ctx, params):
        """
        :param params: instance of type "SearchFamiliesFromCG" -> structure:
           parameter "comparison_genome_ref" of String, parameter "query" of
           String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchFamiliesFromCGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "families" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "families" of list of
           type "GenomeComparisonFamily" (GenomeComparisonFamily object: this
           object holds information about a protein family across a set of
           genomes) -> structure: parameter "core" of Long, parameter
           "genome_features" of mapping from String to list of tuple of size
           3: type "Feature_id", list of Long, Double, parameter "id" of
           String, parameter "type" of String, parameter
           "protein_translation" of String, parameter "number_genomes" of
           Long, parameter "fraction_genomes" of Double, parameter
           "fraction_consistent_annotations" of Double, parameter
           "most_consistent_role" of String, parameter "num_found" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_families_from_comparison_genome
        result = self.indexer.search_families_from_comparison_genome(
                                                          ctx["token"],
                                                          params.get("comparison_genome_ref", None),
                                                          params.get("query", None),
                                                          params.get("sort_by", None),
                                                          params.get("start", None),
                                                          params.get("limit", None),
                                                          params.get("num_found", None))
        #END search_families_from_comparison_genome

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_families_from_comparison_genome return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def search_functions_from_comparison_genome(self, ctx, params):
        """
        :param params: instance of type "SearchFunctionsFromCG" -> structure:
           parameter "comparison_genome_ref" of String, parameter "query" of
           String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchFunctionsFromCGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "functions" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "functions" of list
           of type "GenomeComparisonFunction" (GenomeComparisonFunction
           object: this object holds information about a genome in a function
           across all genomes) -> structure: parameter "core" of Long,
           parameter "genome_features" of mapping from String to list of
           tuple of size 3: type "Feature_id", Long, Double, parameter "id"
           of String, parameter "reactions" of list of tuple of size 2: type
           "Reaction_id", String, parameter "subsystem" of String, parameter
           "primclass" of String, parameter "subclass" of String, parameter
           "number_genomes" of Long, parameter "fraction_genomes" of Double,
           parameter "fraction_consistent_families" of Double, parameter
           "most_consistent_family" of String, parameter "num_found" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_functions_from_comparison_genome
        result = self.indexer.search_functions_from_comparison_genome(
                                                          ctx["token"],
                                                          params.get("comparison_genome_ref", None),
                                                          params.get("query", None),
                                                          params.get("sort_by", None),
                                                          params.get("start", None),
                                                          params.get("limit", None),
                                                          params.get("num_found", None))
        #END search_functions_from_comparison_genome

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_functions_from_comparison_genome return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def search_comparison_genome_from_comparison_genome(self, ctx, params):
        """
        :param params: instance of type "SearchComparisonGenomesFromCG" ->
           structure: parameter "comparison_genome_ref" of String, parameter
           "query" of String, parameter "sort_by" of list of type
           "column_sorting" -> tuple of size 2: parameter "column" of String,
           parameter "ascending" of type "boolean" (Indicates true or false
           values, false = 0, true = 1 @range [0,1]), parameter "start" of
           Long, parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchComparisonGenomesFromCGResult"
           (num_found - number of all items found in query search (with only
           part of it returned in "comparison genomes" list).) -> structure:
           parameter "query" of String, parameter "start" of Long, parameter
           "comparison_genomes" of list of type "GenomeComparisonGenome"
           (GenomeComparisonGenome object: this object holds information
           about a genome in a genome comparison) -> structure: parameter
           "id" of String, parameter "genome_ref" of type "Genome_ref",
           parameter "genome_similarity" of mapping from String to tuple of
           size 2: Long, Long, parameter "name" of String, parameter
           "taxonomy" of String, parameter "features" of Long, parameter
           "families" of Long, parameter "functions" of Long, parameter
           "num_found" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN search_comparison_genome_from_comparison_genome
        result = self.indexer.search_comparison_genome_from_comparison_genome(
                                                          ctx["token"],
                                                          params.get("comparison_genome_ref", None),
                                                          params.get("query", None),
                                                          params.get("sort_by", None),
                                                          params.get("start", None),
                                                          params.get("limit", None),
                                                          params.get("num_found", None))
        #END search_comparison_genome_from_comparison_genome

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method search_comparison_genome_from_comparison_genome return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def compute_summary_from_pangenome(self, ctx, params):
        """
        :param params: instance of type "ComputeSummaryFromPG" -> structure:
           parameter "pangenome_ref" of String
        :returns: instance of type "ComputeSummaryFromPGResult" -> structure:
           parameter "families" of mapping from String to Long, parameter
           "genes" of mapping from String to Long, parameter
           "shared_family_map" of mapping from String to mapping from String
           to Long, parameter "genome_ref_name_map" of mapping from String to
           mapping from String to String, parameter "pangenome_id" of String,
           parameter "genomes" of Long
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN compute_summary_from_pangenome
        result = self.indexer.compute_summary_from_pangenome(
                                                          ctx["token"],
                                                          params.get("pangenome_ref", None))
        #END compute_summary_from_pangenome

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method compute_summary_from_pangenome return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
