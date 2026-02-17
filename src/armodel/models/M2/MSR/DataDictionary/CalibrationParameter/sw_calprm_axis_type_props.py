"""SwCalprmAxisTypeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 353)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class SwCalprmAxisTypeProps(ARObject):
    """AUTOSAR SwCalprmAxisTypeProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_gradient": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxGradient
        "monotony": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MonotonyEnum,
        ),  # monotony
    }

    def __init__(self) -> None:
        """Initialize SwCalprmAxisTypeProps."""
        super().__init__()
        self.max_gradient: Optional[Float] = None
        self.monotony: Optional[MonotonyEnum] = None


class SwCalprmAxisTypePropsBuilder:
    """Builder for SwCalprmAxisTypeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxisTypeProps = SwCalprmAxisTypeProps()

    def build(self) -> SwCalprmAxisTypeProps:
        """Build and return SwCalprmAxisTypeProps object.

        Returns:
            SwCalprmAxisTypeProps instance
        """
        # TODO: Add validation
        return self._obj
