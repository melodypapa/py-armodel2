"""AutosarVariableRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class AutosarVariableRef(ARObject):
    """AUTOSAR AutosarVariableRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("autosar_variable", None, False, False, any (ArVariableIn)),  # autosarVariable
        ("local_variable", None, False, False, VariableDataPrototype),  # localVariable
    ]

    def __init__(self) -> None:
        """Initialize AutosarVariableRef."""
        super().__init__()
        self.autosar_variable: Optional[Any] = None
        self.local_variable: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarVariableRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarVariableRef":
        """Create AutosarVariableRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarVariableRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarVariableRef since parent returns ARObject
        return cast("AutosarVariableRef", obj)


class AutosarVariableRefBuilder:
    """Builder for AutosarVariableRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarVariableRef = AutosarVariableRef()

    def build(self) -> AutosarVariableRef:
        """Build and return AutosarVariableRef object.

        Returns:
            AutosarVariableRef instance
        """
        # TODO: Add validation
        return self._obj
