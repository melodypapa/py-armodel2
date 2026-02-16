"""Baseline AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_sdg_defs", None, False, True, SdgDef),  # customSdgDefs
        ("customs", None, False, True, Documentation),  # customs
        ("standards", None, False, True, None),  # standards
    ]

    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_defs: list[SdgDef] = []
        self.customs: list[Documentation] = []
        self.standards: list[String] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Baseline to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Baseline":
        """Create Baseline from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Baseline instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Baseline since parent returns ARObject
        return cast("Baseline", obj)


class BaselineBuilder:
    """Builder for Baseline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Baseline = Baseline()

    def build(self) -> Baseline:
        """Build and return Baseline object.

        Returns:
            Baseline instance
        """
        # TODO: Add validation
        return self._obj
