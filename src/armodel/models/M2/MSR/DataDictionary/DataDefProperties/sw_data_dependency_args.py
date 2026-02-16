"""SwDataDependencyArgs AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)


class SwDataDependencyArgs(ARObject):
    """AUTOSAR SwDataDependencyArgs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_calprm_ref_proxy", None, False, False, SwCalprmRefProxy),  # swCalprmRefProxy
        ("sw_variable_ref_proxy", None, False, False, SwVariableRefProxy),  # swVariableRefProxy
    ]

    def __init__(self) -> None:
        """Initialize SwDataDependencyArgs."""
        super().__init__()
        self.sw_calprm_ref_proxy: Optional[SwCalprmRefProxy] = None
        self.sw_variable_ref_proxy: Optional[SwVariableRefProxy] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwDataDependencyArgs to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependencyArgs":
        """Create SwDataDependencyArgs from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwDataDependencyArgs instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwDataDependencyArgs since parent returns ARObject
        return cast("SwDataDependencyArgs", obj)


class SwDataDependencyArgsBuilder:
    """Builder for SwDataDependencyArgs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependencyArgs = SwDataDependencyArgs()

    def build(self) -> SwDataDependencyArgs:
        """Build and return SwDataDependencyArgs object.

        Returns:
            SwDataDependencyArgs instance
        """
        # TODO: Add validation
        return self._obj
