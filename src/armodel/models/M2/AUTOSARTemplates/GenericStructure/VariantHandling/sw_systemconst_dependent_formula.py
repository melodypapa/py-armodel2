"""SwSystemconstDependentFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstDependentFormula(ARObject):
    """AUTOSAR SwSystemconstDependentFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sysc", None, False, False, SwSystemconst),  # sysc
        ("sysc_string", None, False, False, SwSystemconst),  # syscString
    ]

    def __init__(self) -> None:
        """Initialize SwSystemconstDependentFormula."""
        super().__init__()
        self.sysc: Optional[SwSystemconst] = None
        self.sysc_string: Optional[SwSystemconst] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwSystemconstDependentFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstDependentFormula":
        """Create SwSystemconstDependentFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwSystemconstDependentFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwSystemconstDependentFormula since parent returns ARObject
        return cast("SwSystemconstDependentFormula", obj)


class SwSystemconstDependentFormulaBuilder:
    """Builder for SwSystemconstDependentFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstDependentFormula = SwSystemconstDependentFormula()

    def build(self) -> SwSystemconstDependentFormula:
        """Build and return SwSystemconstDependentFormula object.

        Returns:
            SwSystemconstDependentFormula instance
        """
        # TODO: Add validation
        return self._obj
