"""FlexrayFifoRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FlexrayFifoRange(ARObject):
    """AUTOSAR FlexrayFifoRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "range_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rangeMax
        "range_min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rangeMin
    }

    def __init__(self) -> None:
        """Initialize FlexrayFifoRange."""
        super().__init__()
        self.range_max: Optional[Integer] = None
        self.range_min: Optional[Integer] = None


class FlexrayFifoRangeBuilder:
    """Builder for FlexrayFifoRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFifoRange = FlexrayFifoRange()

    def build(self) -> FlexrayFifoRange:
        """Build and return FlexrayFifoRange object.

        Returns:
            FlexrayFifoRange instance
        """
        # TODO: Add validation
        return self._obj
