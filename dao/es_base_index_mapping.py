es_base_index_mapping = {
    "mappings": {
        "dynamic": "false",
        "properties": {
            "description": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "id": {
                "type": "keyword"
            },
            "metrics": {
                "properties": {
                    "cvssMetricV2": {
                        "properties": {
                            "acInsufInfo": {
                                "type": "boolean"
                            },
                            "baseSeverity": {
                                "type": "keyword"
                            },
                            "cvssData": {
                                "properties": {
                                    "accessComplexity": {
                                        "type": "keyword"
                                    },
                                    "accessVector": {
                                        "type": "keyword"
                                    },
                                    "authentication": {
                                        "type": "keyword"
                                    },
                                    "availabilityImpact": {
                                        "type": "keyword"
                                    },
                                    "baseScore": {
                                        "type": "long"
                                    },
                                    "confidentialityImpact": {
                                        "type": "keyword"
                                    },
                                    "integrityImpact": {
                                        "type": "keyword"
                                    },
                                    "vectorString": {
                                        "type": "keyword"
                                    },
                                    "version": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "exploitabilityScore": {
                                "type": "long"
                            },
                            "impactScore": {
                                "type": "float"
                            },
                            "obtainAllPrivilege": {
                                "type": "boolean"
                            },
                            "obtainOtherPrivilege": {
                                "type": "boolean"
                            },
                            "obtainUserPrivilege": {
                                "type": "boolean"
                            },
                            "source": {
                                "type": "keyword"
                            },
                            "type": {
                                "type": "keyword"
                            },
                            "userInteractionRequired": {
                                "type": "boolean"
                            }
                        }
                    },
                    "cvssMetricV30": {
                        "properties": {
                            "cvssData": {
                                "properties": {
                                    "attackComplexity": {
                                        "type": "keyword"
                                    },
                                    "attackVector": {
                                        "type": "keyword"
                                    },
                                    "availabilityImpact": {
                                        "type": "keyword"
                                    },
                                    "baseScore": {
                                        "type": "float"
                                    },
                                    "baseSeverity": {
                                        "type": "keyword"
                                    },
                                    "confidentialityImpact": {
                                        "type": "keyword"
                                    },
                                    "integrityImpact": {
                                        "type": "keyword"
                                    },
                                    "privilegesRequired": {
                                        "type": "keyword"
                                    },
                                    "scope": {
                                        "type": "keyword"
                                    },
                                    "userInteraction": {
                                        "type": "keyword"
                                    },
                                    "vectorString": {
                                        "type": "keyword"
                                    },
                                    "version": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "exploitabilityScore": {
                                "type": "float"
                            },
                            "impactScore": {
                                "type": "float"
                            },
                            "source": {
                                "type": "keyword"
                            },
                            "type": {
                                "type": "keyword"
                            }
                        }
                    },
                    "cvssMetricV31": {
                        "properties": {
                            "cvssData": {
                                "properties": {
                                    "attackComplexity": {
                                        "type": "keyword"
                                    },
                                    "attackVector": {
                                        "type": "keyword"
                                    },
                                    "availabilityImpact": {
                                        "type": "keyword"
                                    },
                                    "baseScore": {
                                        "type": "float"
                                    },
                                    "baseSeverity": {
                                        "type": "keyword"
                                    },
                                    "confidentialityImpact": {
                                        "type": "keyword"
                                    },
                                    "integrityImpact": {
                                        "type": "keyword"
                                    },
                                    "privilegesRequired": {
                                        "type": "keyword"
                                    },
                                    "scope": {
                                        "type": "keyword"
                                    },
                                    "userInteraction": {
                                        "type": "keyword"
                                    },
                                    "vectorString": {
                                        "type": "keyword"
                                    },
                                    "version": {
                                        "type": "keyword"
                                    }
                                }
                            },
                            "exploitabilityScore": {
                                "type": "float"
                            },
                            "impactScore": {
                                "type": "float"
                            },
                            "source": {
                                "type": "keyword"
                            },
                            "type": {
                                "type": "keyword"
                            }
                        }
                    }
                }
            }
        }
    }
}
