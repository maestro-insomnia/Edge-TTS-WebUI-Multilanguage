import gradio as gr
import edge_tts
import asyncio
import os

from gradio.themes.utils import fonts

# 创建 Soft 主题并指定字体
soft_theme = gr.themes.Soft(font=fonts.GoogleFont("sans-serif"))

# 示例 VOICES 数据结构
VOICES = {
    "Afrikaans": {
        "South Africa": {
            "Female": {
                "General": {
                    "Adri-Friendly, Positive": [
                        "af-ZA-AdriNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Willem-Friendly, Positive": [
                        "af-ZA-WillemNeural"
                    ]
                }
            }
        }
    },
    "Albanian": {
        "Albania": {
            "Female": {
                "General": {
                    "Anila-Friendly, Positive": [
                        "sq-AL-AnilaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Ilir-Friendly, Positive": [
                        "sq-AL-IlirNeural"
                    ]
                }
            }
        }
    },
    "Amharic": {
        "Ethiopia": {
            "Male": {
                "General": {
                    "Ameha-Friendly, Positive": [
                        "am-ET-AmehaNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Mekdes-Friendly, Positive": [
                        "am-ET-MekdesNeural"
                    ]
                }
            }
        }
    },
    "Arabic": {
        "Algeria": {
            "Female": {
                "General": {
                    "Amina-Friendly, Positive": [
                        "ar-DZ-AminaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Ismael-Friendly, Positive": [
                        "ar-DZ-IsmaelNeural"
                    ]
                }
            }
        },
        "Bahrain": {
            "Male": {
                "General": {
                    "Ali-Friendly, Positive": [
                        "ar-BH-AliNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Laila-Friendly, Positive": [
                        "ar-BH-LailaNeural"
                    ]
                }
            }
        },
        "Egypt": {
            "Female": {
                "General": {
                    "Salma-Friendly, Positive": [
                        "ar-EG-SalmaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Shakir-Friendly, Positive": [
                        "ar-EG-ShakirNeural"
                    ]
                }
            }
        },
        "Iraq": {
            "Male": {
                "General": {
                    "Bassel-Friendly, Positive": [
                        "ar-IQ-BasselNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Rana-Friendly, Positive": [
                        "ar-IQ-RanaNeural"
                    ]
                }
            }
        },
        "Jordan": {
            "Female": {
                "General": {
                    "Sana-Friendly, Positive": [
                        "ar-JO-SanaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Taim-Friendly, Positive": [
                        "ar-JO-TaimNeural"
                    ]
                }
            }
        },
        "Kuwait": {
            "Male": {
                "General": {
                    "Fahed-Friendly, Positive": [
                        "ar-KW-FahedNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Noura-Friendly, Positive": [
                        "ar-KW-NouraNeural"
                    ]
                }
            }
        },
        "Lebanon": {
            "Female": {
                "General": {
                    "Layla-Friendly, Positive": [
                        "ar-LB-LaylaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Rami-Friendly, Positive": [
                        "ar-LB-RamiNeural"
                    ]
                }
            }
        },
        "Libya": {
            "Female": {
                "General": {
                    "Iman-Friendly, Positive": [
                        "ar-LY-ImanNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Omar-Friendly, Positive": [
                        "ar-LY-OmarNeural"
                    ]
                }
            }
        },
        "Morocco": {
            "Male": {
                "General": {
                    "Jamal-Friendly, Positive": [
                        "ar-MA-JamalNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Mouna-Friendly, Positive": [
                        "ar-MA-MounaNeural"
                    ]
                }
            }
        },
        "Oman": {
            "Male": {
                "General": {
                    "Abdullah-Friendly, Positive": [
                        "ar-OM-AbdullahNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Aysha-Friendly, Positive": [
                        "ar-OM-AyshaNeural"
                    ]
                }
            }
        },
        "Qatar": {
            "Female": {
                "General": {
                    "Amal-Friendly, Positive": [
                        "ar-QA-AmalNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Moaz-Friendly, Positive": [
                        "ar-QA-MoazNeural"
                    ]
                }
            }
        },
        "Saudi Arabia": {
            "Male": {
                "General": {
                    "Hamed-Friendly, Positive": [
                        "ar-SA-HamedNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Zariyah-Friendly, Positive": [
                        "ar-SA-ZariyahNeural"
                    ]
                }
            }
        },
        "Syrian Arab Republic": {
            "Female": {
                "General": {
                    "Amany-Friendly, Positive": [
                        "ar-SY-AmanyNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Laith-Friendly, Positive": [
                        "ar-SY-LaithNeural"
                    ]
                }
            }
        },
        "Tunisia": {
            "Male": {
                "General": {
                    "Hedi-Friendly, Positive": [
                        "ar-TN-HediNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Reem-Friendly, Positive": [
                        "ar-TN-ReemNeural"
                    ]
                }
            }
        },
        "United Arab Emirates": {
            "Female": {
                "General": {
                    "Fatima-Friendly, Positive": [
                        "ar-AE-FatimaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Hamdan-Friendly, Positive": [
                        "ar-AE-HamdanNeural"
                    ]
                }
            }
        },
        "Yemen": {
            "Female": {
                "General": {
                    "Maryam-Friendly, Positive": [
                        "ar-YE-MaryamNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Saleh-Friendly, Positive": [
                        "ar-YE-SalehNeural"
                    ]
                }
            }
        }
    },
    "Azerbaijani": {
        "Azerbaijan": {
            "Male": {
                "General": {
                    "Babek-Friendly, Positive": [
                        "az-AZ-BabekNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Banu-Friendly, Positive": [
                        "az-AZ-BanuNeural"
                    ]
                }
            }
        }
    },
    "Bengali": {
        "Bangladesh": {
            "Female": {
                "General": {
                    "Nabanita-Friendly, Positive": [
                        "bn-BD-NabanitaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Pradeep-Friendly, Positive": [
                        "bn-BD-PradeepNeural"
                    ]
                }
            }
        },
        "India": {
            "Male": {
                "General": {
                    "Bashkar-Friendly, Positive": [
                        "bn-IN-BashkarNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Tanishaa-Friendly, Positive": [
                        "bn-IN-TanishaaNeural"
                    ]
                }
            }
        }
    },
    "Bosnian": {
        "Bosnia and Herzegovina": {
            "Female": {
                "General": {
                    "Vesna-Friendly, Positive": [
                        "bs-BA-VesnaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Goran-Friendly, Positive": [
                        "bs-BA-GoranNeural"
                    ]
                }
            }
        }
    },
    "Bulgarian": {
        "Bulgaria": {
            "Male": {
                "General": {
                    "Borislav-Friendly, Positive": [
                        "bg-BG-BorislavNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Kalina-Friendly, Positive": [
                        "bg-BG-KalinaNeural"
                    ]
                }
            }
        }
    },
    "Burmese": {
        "Myanmar": {
            "Female": {
                "General": {
                    "Nilar-Friendly, Positive": [
                        "my-MM-NilarNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Thiha-Friendly, Positive": [
                        "my-MM-ThihaNeural"
                    ]
                }
            }
        }
    },
    "Catalan": {
        "Spain": {
            "Male": {
                "General": {
                    "Enric-Friendly, Positive": [
                        "ca-ES-EnricNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Joana-Friendly, Positive": [
                        "ca-ES-JoanaNeural"
                    ]
                }
            }
        }
    },
    "Chinese": {
        "Hong Kong": {
            "Female": {
                "General": {
                    "HiuGaai-Friendly, Positive": [
                        "zh-HK-HiuGaaiNeural"
                    ],
                    "HiuMaan-Friendly, Positive": [
                        "zh-HK-HiuMaanNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "WanLung-Friendly, Positive": [
                        "zh-HK-WanLungNeural"
                    ]
                }
            }
        },
        "China": {
            "Female": {
                "News, Novel": {
                    "Xiaoxiao-Warm": [
                        "zh-CN-XiaoxiaoNeural"
                    ]
                },
                "Cartoon, Novel": {
                    "Xiaoyi-Lively": [
                        "zh-CN-XiaoyiNeural"
                    ]
                },
                "Dialect": {
                    "Xiaobei-Humorous": [
                        "zh-CN-liaoning-XiaobeiNeural"
                    ],
                    "Xiaoni-Bright": [
                        "zh-CN-shaanxi-XiaoniNeural"
                    ]
                }
            },
            "Male": {
                "Sports, Novel": {
                    "Yunjian-Passion": [
                        "zh-CN-YunjianNeural"
                    ]
                },
                "Novel": {
                    "Yunxi-Lively, Sunshine": [
                        "zh-CN-YunxiNeural"
                    ]
                },
                "Cartoon, Novel": {
                    "Yunxia-Cute": [
                        "zh-CN-YunxiaNeural"
                    ]
                },
                "News": {
                    "Yunyang-Professional, Reliable": [
                        "zh-CN-YunyangNeural"
                    ]
                }
            }
        },
        "Taiwan, Province of China": {
            "Female": {
                "General": {
                    "HsiaoChen-Friendly, Positive": [
                        "zh-TW-HsiaoChenNeural"
                    ],
                    "HsiaoYu-Friendly, Positive": [
                        "zh-TW-HsiaoYuNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "YunJhe-Friendly, Positive": [
                        "zh-TW-YunJheNeural"
                    ]
                }
            }
        }
    },
    "Croatian": {
        "Croatia": {
            "Female": {
                "General": {
                    "Gabrijela-Friendly, Positive": [
                        "hr-HR-GabrijelaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Srecko-Friendly, Positive": [
                        "hr-HR-SreckoNeural"
                    ]
                }
            }
        }
    },
    "Czech": {
        "Czechia": {
            "Male": {
                "General": {
                    "Antonin-Friendly, Positive": [
                        "cs-CZ-AntoninNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Vlasta-Friendly, Positive": [
                        "cs-CZ-VlastaNeural"
                    ]
                }
            }
        }
    },
    "Danish": {
        "Denmark": {
            "Female": {
                "General": {
                    "Christel-Friendly, Positive": [
                        "da-DK-ChristelNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Jeppe-Friendly, Positive": [
                        "da-DK-JeppeNeural"
                    ]
                }
            }
        }
    },
    "Dutch": {
        "Belgium": {
            "Male": {
                "General": {
                    "Arnaud-Friendly, Positive": [
                        "nl-BE-ArnaudNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Dena-Friendly, Positive": [
                        "nl-BE-DenaNeural"
                    ]
                }
            }
        },
        "Netherlands": {
            "Female": {
                "General": {
                    "Colette-Friendly, Positive": [
                        "nl-NL-ColetteNeural"
                    ],
                    "Fenna-Friendly, Positive": [
                        "nl-NL-FennaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Maarten-Friendly, Positive": [
                        "nl-NL-MaartenNeural"
                    ]
                }
            }
        }
    },
    "English": {
        "Australia": {
            "Female": {
                "General": {
                    "Natasha-Friendly, Positive": [
                        "en-AU-NatashaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "William-Friendly, Positive": [
                        "en-AU-WilliamNeural"
                    ]
                }
            }
        },
        "Canada": {
            "Female": {
                "General": {
                    "Clara-Friendly, Positive": [
                        "en-CA-ClaraNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Liam-Friendly, Positive": [
                        "en-CA-LiamNeural"
                    ]
                }
            }
        },
        "Hong Kong": {
            "Female": {
                "General": {
                    "Yan-Friendly, Positive": [
                        "en-HK-YanNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Sam-Friendly, Positive": [
                        "en-HK-SamNeural"
                    ]
                }
            }
        },
        "India": {
            "Female": {
                "General": {
                    "Neerja-Friendly, Positive, Expressive": [
                        "en-IN-NeerjaExpressiveNeural"
                    ],
			"Neerja-Friendly, Positive": [
                        "en-IN-NeerjaNeural"]

                }
            },
            "Male": {
                "General": {
                    "Prabhat-Friendly, Positive": [
                        "en-IN-PrabhatNeural"
                    ]
                }
            }
        },
        "Ireland": {
            "Male": {
                "General": {
                    "Connor-Friendly, Positive": [
                        "en-IE-ConnorNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Emily-Friendly, Positive": [
                        "en-IE-EmilyNeural"
                    ]
                }
            }
        },
        "Kenya": {
            "Female": {
                "General": {
                    "Asilia-Friendly, Positive": [
                        "en-KE-AsiliaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Chilemba-Friendly, Positive": [
                        "en-KE-ChilembaNeural"
                    ]
                }
            }
        },
        "New Zealand": {
            "Male": {
                "General": {
                    "Mitchell-Friendly, Positive": [
                        "en-NZ-MitchellNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Molly-Friendly, Positive": [
                        "en-NZ-MollyNeural"
                    ]
                }
            }
        },
        "Nigeria": {
            "Male": {
                "General": {
                    "Abeo-Friendly, Positive": [
                        "en-NG-AbeoNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Ezinne-Friendly, Positive": [
                        "en-NG-EzinneNeural"
                    ]
                }
            }
        },
        "Philippines": {
            "Male": {
                "General": {
                    "James-Friendly, Positive": [
                        "en-PH-JamesNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Rosa-Friendly, Positive": [
                        "en-PH-RosaNeural"
                    ]
                }
            }
        },
        "Singapore": {
            "Female": {
                "General": {
                    "Luna-Friendly, Positive": [
                        "en-SG-LunaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Wayne-Friendly, Positive": [
                        "en-SG-WayneNeural"
                    ]
                }
            }
        },
        "United States": {
            "Female": {
                "Conversation, Copilot": {
                    "AvaMultilingual-Expressive, Caring, Pleasant, Friendly": [
                        "en-US-AvaMultilingualNeural"
                    ],
                    "EmmaMultilingual-Cheerful, Clear, Conversational": [
                        "en-US-EmmaMultilingualNeural"
                    ],
                    "Ava-Expressive, Caring, Pleasant, Friendly": [
                        "en-US-AvaNeural"
                    ],
                    "Emma-Cheerful, Clear, Conversational": [
                        "en-US-EmmaNeural"
                    ]
                },
                "Cartoon, Conversation": {
                    "Ana-Cute": [
                        "en-US-AnaNeural"
                    ]
                },
                "News, Novel": {
                    "Aria-Positive, Confident": [
                        "en-US-AriaNeural"
                    ],
                    "Michelle-Friendly, Pleasant": [
                        "en-US-MichelleNeural"
                    ]
                },
                "General": {
                    "Jenny-Friendly, Considerate, Comfort": [
                        "en-US-JennyNeural"
                    ]
                }
            },
            "Male": {
                "Conversation, Copilot": {
                    "AndrewMultilingual-Warm, Confident, Authentic, Honest": [
                        "en-US-AndrewMultilingualNeural"
                    ],
                    "BrianMultilingual-Approachable, Casual, Sincere": [
                        "en-US-BrianMultilingualNeural"
                    ],
                    "Andrew-Warm, Confident, Authentic, Honest": [
                        "en-US-AndrewNeural"
                    ],
                    "Brian-Approachable, Casual, Sincere": [
                        "en-US-BrianNeural"
                    ]
                },
                "News, Novel": {
                    "Christopher-Reliable, Authority": [
                        "en-US-ChristopherNeural"
                    ],
                    "Eric-Rational": [
                        "en-US-EricNeural"
                    ],
                    "Guy-Passion": [
                        "en-US-GuyNeural"
                    ],
                    "Roger-Lively": [
                        "en-US-RogerNeural"
                    ],
                    "Steffan-Rational": [
                        "en-US-SteffanNeural"
                    ]
                }
            }
        },
        "South Africa": {
            "Female": {
                "General": {
                    "Leah-Friendly, Positive": [
                        "en-ZA-LeahNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Luke-Friendly, Positive": [
                        "en-ZA-LukeNeural"
                    ]
                }
            }
        },
        "Tanzania, United Republic of": {
            "Male": {
                "General": {
                    "Elimu-Friendly, Positive": [
                        "en-TZ-ElimuNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Imani-Friendly, Positive": [
                        "en-TZ-ImaniNeural"
                    ]
                }
            }
        },
        "United Kingdom": {
            "Female": {
                "General": {
                    "Libby-Friendly, Positive": [
                        "en-GB-LibbyNeural"
                    ],
                    "Maisie-Friendly, Positive": [
                        "en-GB-MaisieNeural"
                    ],
                    "Sonia-Friendly, Positive": [
                        "en-GB-SoniaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Ryan-Friendly, Positive": [
                        "en-GB-RyanNeural"
                    ],
                    "Thomas-Friendly, Positive": [
                        "en-GB-ThomasNeural"
                    ]
                }
            }
        }
    },
    "Estonian": {
        "Estonia": {
            "Female": {
                "General": {
                    "Anu-Friendly, Positive": [
                        "et-EE-AnuNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Kert-Friendly, Positive": [
                        "et-EE-KertNeural"
                    ]
                }
            }
        }
    },
    "Filipino": {
        "Philippines": {
            "Male": {
                "General": {
                    "Angelo-Friendly, Positive": [
                        "fil-PH-AngeloNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Blessica-Friendly, Positive": [
                        "fil-PH-BlessicaNeural"
                    ]
                }
            }
        }
    },
    "Finnish": {
        "Finland": {
            "Male": {
                "General": {
                    "Harri-Friendly, Positive": [
                        "fi-FI-HarriNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Noora-Friendly, Positive": [
                        "fi-FI-NooraNeural"
                    ]
                }
            }
        }
    },
    "French": {
        "Belgium": {
            "Female": {
                "General": {
                    "Charline-Friendly, Positive": [
                        "fr-BE-CharlineNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Gerard-Friendly, Positive": [
                        "fr-BE-GerardNeural"
                    ]
                }
            }
        },
        "Canada": {
            "Male": {
                "General": {
                    "Thierry-Friendly, Positive": [
                        "fr-CA-ThierryNeural"
                    ],
                    "Antoine-Friendly, Positive": [
                        "fr-CA-AntoineNeural"
                    ],
                    "Jean-Friendly, Positive": [
                        "fr-CA-JeanNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sylvie-Friendly, Positive": [
                        "fr-CA-SylvieNeural"
                    ]
                }
            }
        },
        "France": {
            "Female": {
                "General": {
                    "VivienneMultilingual-Friendly, Positive": [
                        "fr-FR-VivienneMultilingualNeural"
                    ],
                    "Denise-Friendly, Positive": [
                        "fr-FR-DeniseNeural"
                    ],
                    "Eloise-Friendly, Positive": [
                        "fr-FR-EloiseNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "RemyMultilingual-Friendly, Positive": [
                        "fr-FR-RemyMultilingualNeural"
                    ],
                    "Henri-Friendly, Positive": [
                        "fr-FR-HenriNeural"
                    ]
                }
            }
        },
        "Switzerland": {
            "Female": {
                "General": {
                    "Ariane-Friendly, Positive": [
                        "fr-CH-ArianeNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Fabrice-Friendly, Positive": [
                        "fr-CH-FabriceNeural"
                    ]
                }
            }
        }
    },
    "Galician": {
        "Spain": {
            "Male": {
                "General": {
                    "Roi-Friendly, Positive": [
                        "gl-ES-RoiNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sabela-Friendly, Positive": [
                        "gl-ES-SabelaNeural"
                    ]
                }
            }
        }
    },
    "Georgian": {
        "Georgia": {
            "Female": {
                "General": {
                    "Eka-Friendly, Positive": [
                        "ka-GE-EkaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Giorgi-Friendly, Positive": [
                        "ka-GE-GiorgiNeural"
                    ]
                }
            }
        }
    },
    "German": {
        "Austria": {
            "Female": {
                "General": {
                    "Ingrid-Friendly, Positive": [
                        "de-AT-IngridNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Jonas-Friendly, Positive": [
                        "de-AT-JonasNeural"
                    ]
                }
            }
        },
        "Germany": {
            "Female": {
                "General": {
                    "SeraphinaMultilingual-Friendly, Positive": [
                        "de-DE-SeraphinaMultilingualNeural"
                    ],
                    "Amala-Friendly, Positive": [
                        "de-DE-AmalaNeural"
                    ],
                    "Katja-Friendly, Positive": [
                        "de-DE-KatjaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "FlorianMultilingual-Friendly, Positive": [
                        "de-DE-FlorianMultilingualNeural"
                    ],
                    "Conrad-Friendly, Positive": [
                        "de-DE-ConradNeural"
                    ],
                    "Killian-Friendly, Positive": [
                        "de-DE-KillianNeural"
                    ]
                }
            }
        },
        "Switzerland": {
            "Male": {
                "General": {
                    "Jan-Friendly, Positive": [
                        "de-CH-JanNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Leni-Friendly, Positive": [
                        "de-CH-LeniNeural"
                    ]
                }
            }
        }
    },
    "Greek": {
        "Greece": {
            "Female": {
                "General": {
                    "Athina-Friendly, Positive": [
                        "el-GR-AthinaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Nestoras-Friendly, Positive": [
                        "el-GR-NestorasNeural"
                    ]
                }
            }
        }
    },
    "Gujarati": {
        "India": {
            "Female": {
                "General": {
                    "Dhwani-Friendly, Positive": [
                        "gu-IN-DhwaniNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Niranjan-Friendly, Positive": [
                        "gu-IN-NiranjanNeural"
                    ]
                }
            }
        }
    },
    "Hebrew": {
        "Israel": {
            "Male": {
                "General": {
                    "Avri-Friendly, Positive": [
                        "he-IL-AvriNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Hila-Friendly, Positive": [
                        "he-IL-HilaNeural"
                    ]
                }
            }
        }
    },
    "Hindi": {
        "India": {
            "Male": {
                "General": {
                    "Madhur-Friendly, Positive": [
                        "hi-IN-MadhurNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Swara-Friendly, Positive": [
                        "hi-IN-SwaraNeural"
                    ]
                }
            }
        }
    },
    "Hungarian": {
        "Hungary": {
            "Female": {
                "General": {
                    "Noemi-Friendly, Positive": [
                        "hu-HU-NoemiNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Tamas-Friendly, Positive": [
                        "hu-HU-TamasNeural"
                    ]
                }
            }
        }
    },
    "Icelandic": {
        "Iceland": {
            "Female": {
                "General": {
                    "Gudrun-Friendly, Positive": [
                        "is-IS-GudrunNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Gunnar-Friendly, Positive": [
                        "is-IS-GunnarNeural"
                    ]
                }
            }
        }
    },
    "Indonesian": {
        "Indonesia": {
            "Male": {
                "General": {
                    "Ardi-Friendly, Positive": [
                        "id-ID-ArdiNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Gadis-Friendly, Positive": [
                        "id-ID-GadisNeural"
                    ]
                }
            }
        }
    },
    "Irish": {
        "Ireland": {
            "Male": {
                "General": {
                    "Colm-Friendly, Positive": [
                        "ga-IE-ColmNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Orla-Friendly, Positive": [
                        "ga-IE-OrlaNeural"
                    ]
                }
            }
        }
    },
    "Italian": {
        "Italy": {
            "Male": {
                "General": {
                    "GiuseppeMultilingual-Friendly, Positive": [
                        "it-IT-GiuseppeMultilingualNeural"
                    ],
                    "Diego-Friendly, Positive": [
                        "it-IT-DiegoNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Elsa-Friendly, Positive": [
                        "it-IT-ElsaNeural"
                    ],
                    "Isabella-Friendly, Positive": [
                        "it-IT-IsabellaNeural"
                    ]
                }
            }
        }
    },
    "Japanese": {
        "Japan": {
            "Male": {
                "General": {
                    "Keita-Friendly, Positive": [
                        "ja-JP-KeitaNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Nanami-Friendly, Positive": [
                        "ja-JP-NanamiNeural"
                    ]
                }
            }
        }
    },
    "Javanese": {
        "Indonesia": {
            "Male": {
                "General": {
                    "Dimas-Friendly, Positive": [
                        "jv-ID-DimasNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Siti-Friendly, Positive": [
                        "jv-ID-SitiNeural"
                    ]
                }
            }
        }
    },
    "Kannada": {
        "India": {
            "Male": {
                "General": {
                    "Gagan-Friendly, Positive": [
                        "kn-IN-GaganNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sapna-Friendly, Positive": [
                        "kn-IN-SapnaNeural"
                    ]
                }
            }
        }
    },
    "Kazakh": {
        "Kazakhstan": {
            "Female": {
                "General": {
                    "Aigul-Friendly, Positive": [
                        "kk-KZ-AigulNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Daulet-Friendly, Positive": [
                        "kk-KZ-DauletNeural"
                    ]
                }
            }
        }
    },
    "Khmer": {
        "Cambodia": {
            "Male": {
                "General": {
                    "Piseth-Friendly, Positive": [
                        "km-KH-PisethNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sreymom-Friendly, Positive": [
                        "km-KH-SreymomNeural"
                    ]
                }
            }
        }
    },
    "Korean": {
        "Korea, Republic of": {
            "Male": {
                "General": {
                    "HyunsuMultilingual-Friendly, Positive": [
                        "ko-KR-HyunsuMultilingualNeural"
                    ],
                    "InJoon-Friendly, Positive": [
                        "ko-KR-InJoonNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "SunHi-Friendly, Positive": [
                        "ko-KR-SunHiNeural"
                    ]
                }
            }
        }
    },
    "Lao": {
        "Lao People's Democratic Republic": {
            "Male": {
                "General": {
                    "Chanthavong-Friendly, Positive": [
                        "lo-LA-ChanthavongNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Keomany-Friendly, Positive": [
                        "lo-LA-KeomanyNeural"
                    ]
                }
            }
        }
    },
    "Latvian": {
        "Latvia": {
            "Female": {
                "General": {
                    "Everita-Friendly, Positive": [
                        "lv-LV-EveritaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Nils-Friendly, Positive": [
                        "lv-LV-NilsNeural"
                    ]
                }
            }
        }
    },
    "Lithuanian": {
        "Lithuania": {
            "Male": {
                "General": {
                    "Leonas-Friendly, Positive": [
                        "lt-LT-LeonasNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Ona-Friendly, Positive": [
                        "lt-LT-OnaNeural"
                    ]
                }
            }
        }
    },
    "Macedonian": {
        "North Macedonia": {
            "Male": {
                "General": {
                    "Aleksandar-Friendly, Positive": [
                        "mk-MK-AleksandarNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Marija-Friendly, Positive": [
                        "mk-MK-MarijaNeural"
                    ]
                }
            }
        }
    },
    "Malay": {
        "Malaysia": {
            "Male": {
                "General": {
                    "Osman-Friendly, Positive": [
                        "ms-MY-OsmanNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Yasmin-Friendly, Positive": [
                        "ms-MY-YasminNeural"
                    ]
                }
            }
        }
    },
    "Malayalam": {
        "India": {
            "Male": {
                "General": {
                    "Midhun-Friendly, Positive": [
                        "ml-IN-MidhunNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sobhana-Friendly, Positive": [
                        "ml-IN-SobhanaNeural"
                    ]
                }
            }
        }
    },
    "Maltese": {
        "Malta": {
            "Female": {
                "General": {
                    "Grace-Friendly, Positive": [
                        "mt-MT-GraceNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Joseph-Friendly, Positive": [
                        "mt-MT-JosephNeural"
                    ]
                }
            }
        }
    },
    "Marathi": {
        "India": {
            "Female": {
                "General": {
                    "Aarohi-Friendly, Positive": [
                        "mr-IN-AarohiNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Manohar-Friendly, Positive": [
                        "mr-IN-ManoharNeural"
                    ]
                }
            }
        }
    },
    "Mongolian": {
        "Mongolia": {
            "Male": {
                "General": {
                    "Bataa-Friendly, Positive": [
                        "mn-MN-BataaNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Yesui-Friendly, Positive": [
                        "mn-MN-YesuiNeural"
                    ]
                }
            }
        }
    },
    "Nepali": {
        "Nepal": {
            "Female": {
                "General": {
                    "Hemkala-Friendly, Positive": [
                        "ne-NP-HemkalaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Sagar-Friendly, Positive": [
                        "ne-NP-SagarNeural"
                    ]
                }
            }
        }
    },
    "Norwegian": {
        "Norway": {
            "Male": {
                "General": {
                    "Finn-Friendly, Positive": [
                        "nb-NO-FinnNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Pernille-Friendly, Positive": [
                        "nb-NO-PernilleNeural"
                    ]
                }
            }
        }
    },
    "Pashto": {
        "Afghanistan": {
            "Male": {
                "General": {
                    "GulNawaz-Friendly, Positive": [
                        "ps-AF-GulNawazNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Latifa-Friendly, Positive": [
                        "ps-AF-LatifaNeural"
                    ]
                }
            }
        }
    },
    "Persian": {
        "Iran, Islamic Republic of": {
            "Female": {
                "General": {
                    "Dilara-Friendly, Positive": [
                        "fa-IR-DilaraNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Farid-Friendly, Positive": [
                        "fa-IR-FaridNeural"
                    ]
                }
            }
        }
    },
    "Polish": {
        "Poland": {
            "Male": {
                "General": {
                    "Marek-Friendly, Positive": [
                        "pl-PL-MarekNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Zofia-Friendly, Positive": [
                        "pl-PL-ZofiaNeural"
                    ]
                }
            }
        }
    },
    "Portuguese": {
        "Brazil": {
            "Female": {
                "General": {
                    "ThalitaMultilingual-Friendly, Positive": [
                        "pt-BR-ThalitaMultilingualNeural"
                    ],
                    "Francisca-Friendly, Positive": [
                        "pt-BR-FranciscaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Antonio-Friendly, Positive": [
                        "pt-BR-AntonioNeural"
                    ]
                }
            }
        },
        "Portugal": {
            "Male": {
                "General": {
                    "Duarte-Friendly, Positive": [
                        "pt-PT-DuarteNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Raquel-Friendly, Positive": [
                        "pt-PT-RaquelNeural"
                    ]
                }
            }
        }
    },
    "Romanian": {
        "Romania": {
            "Female": {
                "General": {
                    "Alina-Friendly, Positive": [
                        "ro-RO-AlinaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Emil-Friendly, Positive": [
                        "ro-RO-EmilNeural"
                    ]
                }
            }
        }
    },
    "Russian": {
        "Russian Federation": {
            "Male": {
                "General": {
                    "Dmitry-Friendly, Positive": [
                        "ru-RU-DmitryNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Svetlana-Friendly, Positive": [
                        "ru-RU-SvetlanaNeural"
                    ]
                }
            }
        }
    },
    "Serbian": {
        "Serbia": {
            "Male": {
                "General": {
                    "Nicholas-Friendly, Positive": [
                        "sr-RS-NicholasNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sophie-Friendly, Positive": [
                        "sr-RS-SophieNeural"
                    ]
                }
            }
        }
    },
    "Sinhala": {
        "Sri Lanka": {
            "Male": {
                "General": {
                    "Sameera-Friendly, Positive": [
                        "si-LK-SameeraNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Thilini-Friendly, Positive": [
                        "si-LK-ThiliniNeural"
                    ]
                }
            }
        }
    },
    "Slovak": {
        "Slovakia": {
            "Male": {
                "General": {
                    "Lukas-Friendly, Positive": [
                        "sk-SK-LukasNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Viktoria-Friendly, Positive": [
                        "sk-SK-ViktoriaNeural"
                    ]
                }
            }
        }
    },
    "Slovenian": {
        "Slovenia": {
            "Female": {
                "General": {
                    "Petra-Friendly, Positive": [
                        "sl-SI-PetraNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Rok-Friendly, Positive": [
                        "sl-SI-RokNeural"
                    ]
                }
            }
        }
    },
    "Somali": {
        "Somalia": {
            "Male": {
                "General": {
                    "Muuse-Friendly, Positive": [
                        "so-SO-MuuseNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Ubax-Friendly, Positive": [
                        "so-SO-UbaxNeural"
                    ]
                }
            }
        }
    },
    "Spanish": {
        "Argentina": {
            "Female": {
                "General": {
                    "Elena-Friendly, Positive": [
                        "es-AR-ElenaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Tomas-Friendly, Positive": [
                        "es-AR-TomasNeural"
                    ]
                }
            }
        },
        "Bolivia, Plurinational State of": {
            "Male": {
                "General": {
                    "Marcelo-Friendly, Positive": [
                        "es-BO-MarceloNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sofia-Friendly, Positive": [
                        "es-BO-SofiaNeural"
                    ]
                }
            }
        },
        "Chile": {
            "Female": {
                "General": {
                    "Catalina-Friendly, Positive": [
                        "es-CL-CatalinaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Lorenzo-Friendly, Positive": [
                        "es-CL-LorenzoNeural"
                    ]
                }
            }
        },
        "Colombia": {
            "Male": {
                "General": {
                    "Gonzalo-Friendly, Positive": [
                        "es-CO-GonzaloNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Salome-Friendly, Positive": [
                        "es-CO-SalomeNeural"
                    ]
                }
            }
        },
        "Spain": {
            "Female": {
                "General": {
                    "Ximena-Friendly, Positive": [
                        "es-ES-XimenaNeural"
                    ],
                    "Elvira-Friendly, Positive": [
                        "es-ES-ElviraNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Alvaro-Friendly, Positive": [
                        "es-ES-AlvaroNeural"
                    ]
                }
            }
        },
        "Costa Rica": {
            "Male": {
                "General": {
                    "Juan-Friendly, Positive": [
                        "es-CR-JuanNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Maria-Friendly, Positive": [
                        "es-CR-MariaNeural"
                    ]
                }
            }
        },
        "Cuba": {
            "Female": {
                "General": {
                    "Belkys-Friendly, Positive": [
                        "es-CU-BelkysNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Manuel-Friendly, Positive": [
                        "es-CU-ManuelNeural"
                    ]
                }
            }
        },
        "Dominican Republic": {
            "Male": {
                "General": {
                    "Emilio-Friendly, Positive": [
                        "es-DO-EmilioNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Ramona-Friendly, Positive": [
                        "es-DO-RamonaNeural"
                    ]
                }
            }
        },
        "Ecuador": {
            "Female": {
                "General": {
                    "Andrea-Friendly, Positive": [
                        "es-EC-AndreaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Luis-Friendly, Positive": [
                        "es-EC-LuisNeural"
                    ]
                }
            }
        },
        "El Salvador": {
            "Female": {
                "General": {
                    "Lorena-Friendly, Positive": [
                        "es-SV-LorenaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Rodrigo-Friendly, Positive": [
                        "es-SV-RodrigoNeural"
                    ]
                }
            }
        },
        "Equatorial Guinea": {
            "Male": {
                "General": {
                    "Javier-Friendly, Positive": [
                        "es-GQ-JavierNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Teresa-Friendly, Positive": [
                        "es-GQ-TeresaNeural"
                    ]
                }
            }
        },
        "Guatemala": {
            "Male": {
                "General": {
                    "Andres-Friendly, Positive": [
                        "es-GT-AndresNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Marta-Friendly, Positive": [
                        "es-GT-MartaNeural"
                    ]
                }
            }
        },
        "Honduras": {
            "Male": {
                "General": {
                    "Carlos-Friendly, Positive": [
                        "es-HN-CarlosNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Karla-Friendly, Positive": [
                        "es-HN-KarlaNeural"
                    ]
                }
            }
        },
        "Mexico": {
            "Female": {
                "General": {
                    "Dalia-Friendly, Positive": [
                        "es-MX-DaliaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Jorge-Friendly, Positive": [
                        "es-MX-JorgeNeural"
                    ]
                }
            }
        },
        "Nicaragua": {
            "Male": {
                "General": {
                    "Federico-Friendly, Positive": [
                        "es-NI-FedericoNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Yolanda-Friendly, Positive": [
                        "es-NI-YolandaNeural"
                    ]
                }
            }
        },
        "Panama": {
            "Female": {
                "General": {
                    "Margarita-Friendly, Positive": [
                        "es-PA-MargaritaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Roberto-Friendly, Positive": [
                        "es-PA-RobertoNeural"
                    ]
                }
            }
        },
        "Paraguay": {
            "Male": {
                "General": {
                    "Mario-Friendly, Positive": [
                        "es-PY-MarioNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Tania-Friendly, Positive": [
                        "es-PY-TaniaNeural"
                    ]
                }
            }
        },
        "Peru": {
            "Male": {
                "General": {
                    "Alex-Friendly, Positive": [
                        "es-PE-AlexNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Camila-Friendly, Positive": [
                        "es-PE-CamilaNeural"
                    ]
                }
            }
        },
        "Puerto Rico": {
            "Female": {
                "General": {
                    "Karina-Friendly, Positive": [
                        "es-PR-KarinaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Victor-Friendly, Positive": [
                        "es-PR-VictorNeural"
                    ]
                }
            }
        },
        "United States": {
            "Male": {
                "General": {
                    "Alonso-Friendly, Positive": [
                        "es-US-AlonsoNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Paloma-Friendly, Positive": [
                        "es-US-PalomaNeural"
                    ]
                }
            }
        },
        "Uruguay": {
            "Male": {
                "General": {
                    "Mateo-Friendly, Positive": [
                        "es-UY-MateoNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Valentina-Friendly, Positive": [
                        "es-UY-ValentinaNeural"
                    ]
                }
            }
        },
        "Venezuela, Bolivarian Republic of": {
            "Female": {
                "General": {
                    "Paola-Friendly, Positive": [
                        "es-VE-PaolaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Sebastian-Friendly, Positive": [
                        "es-VE-SebastianNeural"
                    ]
                }
            }
        }
    },
    "Sundanese": {
        "Indonesia": {
            "Male": {
                "General": {
                    "Jajang-Friendly, Positive": [
                        "su-ID-JajangNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Tuti-Friendly, Positive": [
                        "su-ID-TutiNeural"
                    ]
                }
            }
        }
    },
    "Swahili": {
        "Kenya": {
            "Male": {
                "General": {
                    "Rafiki-Friendly, Positive": [
                        "sw-KE-RafikiNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Zuri-Friendly, Positive": [
                        "sw-KE-ZuriNeural"
                    ]
                }
            }
        },
        "Tanzania, United Republic of": {
            "Male": {
                "General": {
                    "Daudi-Friendly, Positive": [
                        "sw-TZ-DaudiNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Rehema-Friendly, Positive": [
                        "sw-TZ-RehemaNeural"
                    ]
                }
            }
        }
    },
    "Swedish": {
        "Sweden": {
            "Male": {
                "General": {
                    "Mattias-Friendly, Positive": [
                        "sv-SE-MattiasNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Sofie-Friendly, Positive": [
                        "sv-SE-SofieNeural"
                    ]
                }
            }
        }
    },
    "Tamil": {
        "India": {
            "Female": {
                "General": {
                    "Pallavi-Friendly, Positive": [
                        "ta-IN-PallaviNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Valluvar-Friendly, Positive": [
                        "ta-IN-ValluvarNeural"
                    ]
                }
            }
        },
        "Malaysia": {
            "Female": {
                "General": {
                    "Kani-Friendly, Positive": [
                        "ta-MY-KaniNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Surya-Friendly, Positive": [
                        "ta-MY-SuryaNeural"
                    ]
                }
            }
        },
        "Singapore": {
            "Male": {
                "General": {
                    "Anbu-Friendly, Positive": [
                        "ta-SG-AnbuNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Venba-Friendly, Positive": [
                        "ta-SG-VenbaNeural"
                    ]
                }
            }
        },
        "Sri Lanka": {
            "Male": {
                "General": {
                    "Kumar-Friendly, Positive": [
                        "ta-LK-KumarNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Saranya-Friendly, Positive": [
                        "ta-LK-SaranyaNeural"
                    ]
                }
            }
        }
    },
    "Telugu": {
        "India": {
            "Male": {
                "General": {
                    "Mohan-Friendly, Positive": [
                        "te-IN-MohanNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Shruti-Friendly, Positive": [
                        "te-IN-ShrutiNeural"
                    ]
                }
            }
        }
    },
    "Thai": {
        "Thailand": {
            "Male": {
                "General": {
                    "Niwat-Friendly, Positive": [
                        "th-TH-NiwatNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Premwadee-Friendly, Positive": [
                        "th-TH-PremwadeeNeural"
                    ]
                }
            }
        }
    },
    "Turkish": {
        "Turkiye": {
            "Female": {
                "General": {
                    "Emel-Friendly, Positive": [
                        "tr-TR-EmelNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Ahmet-Friendly, Positive": [
                        "tr-TR-AhmetNeural"
                    ]
                }
            }
        }
    },
    "Ukrainian": {
        "Ukraine": {
            "Male": {
                "General": {
                    "Ostap-Friendly, Positive": [
                        "uk-UA-OstapNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Polina-Friendly, Positive": [
                        "uk-UA-PolinaNeural"
                    ]
                }
            }
        }
    },
    "Urdu": {
        "India": {
            "Female": {
                "General": {
                    "Gul-Friendly, Positive": [
                        "ur-IN-GulNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Salman-Friendly, Positive": [
                        "ur-IN-SalmanNeural"
                    ]
                }
            }
        },
        "Pakistan": {
            "Male": {
                "General": {
                    "Asad-Friendly, Positive": [
                        "ur-PK-AsadNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Uzma-Friendly, Positive": [
                        "ur-PK-UzmaNeural"
                    ]
                }
            }
        }
    },
    "Uzbek": {
        "Uzbekistan": {
            "Female": {
                "General": {
                    "Madina-Friendly, Positive": [
                        "uz-UZ-MadinaNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Sardor-Friendly, Positive": [
                        "uz-UZ-SardorNeural"
                    ]
                }
            }
        }
    },
    "Vietnamese": {
        "Viet Nam": {
            "Female": {
                "General": {
                    "HoaiMy-Friendly, Positive": [
                        "vi-VN-HoaiMyNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "NamMinh-Friendly, Positive": [
                        "vi-VN-NamMinhNeural"
                    ]
                }
            }
        }
    },
    "Welsh": {
        "United Kingdom": {
            "Male": {
                "General": {
                    "Aled-Friendly, Positive": [
                        "cy-GB-AledNeural"
                    ]
                }
            },
            "Female": {
                "General": {
                    "Nia-Friendly, Positive": [
                        "cy-GB-NiaNeural"
                    ]
                }
            }
        }
    },
    "Zulu": {
        "South Africa": {
            "Female": {
                "General": {
                    "Thando-Friendly, Positive": [
                        "zu-ZA-ThandoNeural"
                    ]
                }
            },
            "Male": {
                "General": {
                    "Themba-Friendly, Positive": [
                        "zu-ZA-ThembaNeural"
                    ]
                }
            }
        }
    }
}

# 获取默认值
default_language = "Chinese"
default_country = "China"
default_gender = "Female"
default_category = "News, Novel"
default_name = "Xiaoxiao-Warm"
default_code = "zh-CN-XiaoxiaoNeural"

# 获取默认 choices
default_choices_countries = list(VOICES[default_language].keys())
default_choices_genders = list(VOICES[default_language][default_country].keys())
default_choices_categories = list(VOICES[default_language][default_country][default_gender].keys())
default_choices_names = list(VOICES[default_language][default_country][default_gender][default_category].keys())

# 更新函数
def update_countries(language, current_country):
    countries = list(VOICES[language].keys())
    if current_country in countries:
        country = current_country
    else:
        country = countries[0] if countries else None
    return gr.update(choices=countries, value=country, allow_custom_value=False)

def update_genders(language, country, current_gender):
    genders = list(VOICES[language][country].keys())
    # If the current gender is in the list of new gender options, keep it
    if current_gender in genders:
        gender = current_gender
    else:
        gender = genders[0] if genders else None
    return gr.update(choices=genders, value=gender, allow_custom_value=False)

def update_categories(language, country, gender, current_category):
    categories = list(VOICES[language][country][gender].keys())
    if current_category in categories:
        category = current_category
    else:
        category = categories[0] if categories else None
    return gr.update(choices=categories, value=category, allow_custom_value=False)

def update_names(language, country, gender, category):
    names = list(VOICES[language][country][gender][category].keys())
    name = names[0] if names else None
    return gr.update(choices=names, value=name, allow_custom_value=False)

def update_code(language, country, gender, category, name):
    code = VOICES[language][country][gender][category][name][0]
    return gr.update(value=code)

# **试听路径**
def changeVoice(language, code):
    example_file = os.path.join(os.path.dirname(__file__), f"example/{language}/{code}.mp3")
    return example_file if os.path.exists(example_file) else None

# 文本转语音
async def textToSpeech(text, code, rate, volume, pitch):
    output_file = "output.mp3"
    rateparam = f"{'+' if rate >= 0 else ''}{rate}%"
    volumeparam = f"{'+' if volume >= 0 else ''}{volume}%"
    pitchparam = f"{'+' if pitch >= 0 else ''}{pitch}Hz"

    communicate = edge_tts.Communicate(text, code, rate=rateparam, volume=volumeparam, pitch=pitchparam, proxy=None)
    await communicate.save(output_file)

    if os.path.exists(output_file):
        return output_file
    else:
        raise gr.Error("转换失败！(Conversion failed!)")

# 清除转换结果
def clearSpeech():
    output_file = "output.mp3"
    if os.path.exists(output_file):
        os.remove(output_file)
    return None, None

# Gradio 界面
with gr.Blocks(css="style.css", title="MS Edge TTS", theme=soft_theme) as demo:
    gr.Markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 30px; font-weight: bold;'>Microsoft Edge TTS</h1>
        <p style='font-size: 12px; line-height: 1.4; margin-top: 5px;'>调用edge-tts进行转换 (Call edge-tts for conversion)</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column():
            with gr.Row():
                language = gr.Dropdown(label="语言 (Language)", choices=list(VOICES.keys()), value=default_language, interactive=True)
                country = gr.Dropdown(label="国家/地区 (Country/Region)", choices=default_choices_countries, value=default_country, interactive=True)
            with gr.Row():
                gender = gr.Dropdown(label="性别 (Gender)", choices=default_choices_genders, value=default_gender, interactive=True)
                category = gr.Dropdown(label="类型 (Category)", choices=default_choices_categories, value=default_category, interactive=True)
                code = gr.Textbox(label="Voice Code", value=default_code, visible=False)

            with gr.Row():
                name = gr.Dropdown(label="发音人 (Name)", choices=default_choices_names, value=default_name, interactive=True)
            with gr.Row():
                example = gr.Audio(label="试听 (Sample)", value=f"example/{default_language}/{VOICES[default_language][default_country][default_gender][default_category][default_name][0]}.mp3", interactive=False)
                # 依次更新各个组件，确保先更新上层组件，再更新下层组件
                language.change(update_countries, inputs=[language, country], outputs=country
                                ).then(update_genders, inputs=[language, country, gender], outputs=gender
                                       ).then(update_categories, inputs=[language, country, gender, category], outputs=category
                                              ).then(update_names, inputs=[language, country, gender, category], outputs=name
                                                     ).then(update_code, inputs=[language, country, gender, category, name], outputs=code
                                                            ).then(changeVoice, inputs=[language, code], outputs=example)

                country.change(update_genders, inputs=[language, country, gender], outputs=gender
                               ).then(update_categories, inputs=[language, country, gender, category], outputs=category
                                      ).then(update_names, inputs=[language, country, gender, category], outputs=name
                                             ).then(update_code, inputs=[language, country, gender, category, name], outputs=code
                                                    ).then(changeVoice, inputs=[language, code], outputs=example)

                gender.change(update_categories, inputs=[language, country, gender, category], outputs=category
                              ).then(update_names, inputs=[language, country, gender, category], outputs=name
                                     ).then(update_code, inputs=[language, country, gender, category, name], outputs=code
                                            ).then(changeVoice, inputs=[language, code], outputs=example)

                category.change(update_names, inputs=[language, country, gender, category], outputs=name
                                ).then(update_code, inputs=[language, country, gender, category, name], outputs=code
                                       ).then(changeVoice, inputs=[language, code], outputs=example)

                name.change(update_code, inputs=[language, country, gender, category, name], outputs=code).then(changeVoice, inputs=[language, code], outputs=example)

            with gr.Row():
                rate = gr.Slider(-100, 100, step=1, value=0, label="语速 (Rate)", info="加快或减慢语速 (Increse or decrease rate)", interactive=True)
            with gr.Row():
                volume = gr.Slider(-100, 100, step=1, value=0, label="音量 (Volume)", info="增大或减小音量 (Increse or decrease volume)", interactive=True)
            with gr.Row():
                pitch = gr.Slider(-100, 100, step=1, value=0, label="音调 (Pitch)", info="增高或降低音调 (Increse or decrease pitch)", interactive=True)
        
        with gr.Column():
            text = gr.TextArea(label="文本 (Text)", info="请输入文本 (Please input your text)")
            btn = gr.Button("生成语音 (Generate Speech)", variant="primary")
            audio = gr.Audio(label="输出 (Output)", interactive=False)
            clear = gr.Button("清除文本和输出 (Clear Text & Output)", variant="primary")

            btn.click(textToSpeech, inputs=[text, code, rate, volume, pitch], outputs=[audio])
            clear.click(clearSpeech, outputs=[text, audio])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
