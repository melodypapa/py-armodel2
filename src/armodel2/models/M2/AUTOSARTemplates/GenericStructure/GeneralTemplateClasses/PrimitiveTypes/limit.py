"""Limit AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 407)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 455)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 196)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import (
    IntervalTypeEnum,
)

# This class represents the ability to express a numerical limit. Note that this is in fact a NumericalVariation Point but has the additional attribute intervalType. Tags: xml.xsd.customType=LIMIT-VALUE xml.xsd.pattern=(0[xX][0-9a-fA-F]+)|(0[0-7]+)|(0[bB][0-1]+)|(([+\-]?[1-9] [0-9]+(\.[0-9]+)?|[+\-]?[0-9](\.[0-9]+)?)([eE]([+\-]?)[0-9]+)?)|\.0|INF|-INF|NaN xml.xsd.type=string
class Limit(ARPrimitive):
    """AUTOSAR Limit primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    interval_type: Optional[IntervalTypeEnum]

    def __init__(self, value: Optional[str] = None, interval_type: Optional[IntervalTypeEnum] = None) -> None:
        """Initialize Limit.

        Args:
            value: The primitive value
            interval_type: intervalType
        """
        super().__init__()
        self.value: Optional[str] = value
        self.interval_type: Optional[IntervalTypeEnum] = interval_type
