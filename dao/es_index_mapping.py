es_index_mapping = {
  "mappings": {
    "properties": {
      "id": {
        "type": "keyword"
      },
      "cveTags": {
        "type": "keyword"
      },
      "description": {
        "type": "text"
      },
      "named_entities": {
        "type": "keyword"
      },
      "metrics": {
        "properties": {
          "cvssMetricV30": {
            "type": "nested",
            "properties": {
              "source": {
                "type": "keyword"
              },
              "type": {
                "type": "keyword"
              },
              "cvssData": {
                "properties": {
                  "version": {
                    "type": "keyword"
                  },
                  "vectorString": {
                    "type": "keyword"
                  },
                  "attackVector": {
                    "type": "keyword"
                  },
                  "attackComplexity": {
                    "type": "keyword"
                  },
                  "privilegesRequired": {
                    "type": "keyword"
                  },
                  "userInteraction": {
                    "type": "keyword"
                  },
                  "scope": {
                    "type": "keyword"
                  },
                  "confidentialityImpact": {
                    "type": "keyword"
                  },
                  "integrityImpact": {
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
                  }
                }
              },
              "exploitabilityScore": {
                "type": "float"
              },
              "impactScore": {
                "type": "float"
              }
            }
          },
          "cvssMetricV31": {
            "type": "nested",
            "properties": {
              "source": {
                "type": "keyword"
              },
              "type": {
                "type": "keyword"
              },
              "cvssData": {
                "properties": {
                  "version": {
                    "type": "keyword"
                  },
                  "vectorString": {
                    "type": "keyword"
                  },
                  "attackVector": {
                    "type": "keyword"
                  },
                  "attackComplexity": {
                    "type": "keyword"
                  },
                  "privilegesRequired": {
                    "type": "keyword"
                  },
                  "userInteraction": {
                    "type": "keyword"
                  },
                  "scope": {
                    "type": "keyword"
                  },
                  "confidentialityImpact": {
                    "type": "keyword"
                  },
                  "integrityImpact": {
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
                  }
                }
              },
              "exploitabilityScore": {
                "type": "float"
              },
              "impactScore": {
                "type": "float"
              }
            }
          },
          "cvssMetricV2": {
            "type": "nested",
            "properties": {
              "source": {
                "type": "keyword"
              },
              "type": {
                "type": "keyword"
              },
              "cvssData": {
                "properties": {
                  "version": {
                    "type": "keyword"
                  },
                  "vectorString": {
                    "type": "keyword"
                  },
                  "accessVector": {
                    "type": "keyword"
                  },
                  "accessComplexity": {
                    "type": "keyword"
                  },
                  "authentication": {
                    "type": "keyword"
                  },
                  "confidentialityImpact": {
                    "type": "keyword"
                  },
                  "integrityImpact": {
                    "type": "keyword"
                  },
                  "availabilityImpact": {
                    "type": "keyword"
                  },
                  "baseScore": {
                    "type": "float"
                  }
                }
              },
              "baseSeverity": {
                "type": "keyword"
              },
              "exploitabilityScore": {
                "type": "float"
              },
              "impactScore": {
                "type": "float"
              }
            }
          }
        }
      }
    }
  }
}
