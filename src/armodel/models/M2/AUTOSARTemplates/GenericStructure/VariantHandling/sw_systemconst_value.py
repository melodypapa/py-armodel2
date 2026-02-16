"""SwSystemconstValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstValue(ARObject):
    """AUTOSAR SwSystemconstValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("annotations", None, False, True, Annotation),  # annotations
        ("sw_systemconst", None, False, False, SwSystemconst),  # swSystemconst
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize SwSystemconstValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.sw_systemconst: SwSystemconst = None
        self.value: Numerical = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwSystemconstValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstValue":
        """Create SwSystemconstValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwSystemconstValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwSystemconstValue since parent returns ARObject
        return cast("SwSystemconstValue", obj)


class SwSystemconstValueBuilder:
    """Builder for SwSystemconstValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstValue = SwSystemconstValue()

    def build(self) -> SwSystemconstValue:
        """Build and return SwSystemconstValue object.

        Returns:
            SwSystemconstValue instance
        """
        # TODO: Add validation
        return self._obj
