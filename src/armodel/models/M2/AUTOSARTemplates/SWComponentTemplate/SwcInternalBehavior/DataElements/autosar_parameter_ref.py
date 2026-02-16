"""AutosarParameterRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarParameterRef(ARObject):
    """AUTOSAR AutosarParameterRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("autosar", None, False, False, DataPrototype),  # autosar
        ("local_parameter", None, False, False, DataPrototype),  # localParameter
    ]

    def __init__(self) -> None:
        """Initialize AutosarParameterRef."""
        super().__init__()
        self.autosar: Optional[DataPrototype] = None
        self.local_parameter: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarParameterRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarParameterRef":
        """Create AutosarParameterRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarParameterRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarParameterRef since parent returns ARObject
        return cast("AutosarParameterRef", obj)


class AutosarParameterRefBuilder:
    """Builder for AutosarParameterRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarParameterRef = AutosarParameterRef()

    def build(self) -> AutosarParameterRef:
        """Build and return AutosarParameterRef object.

        Returns:
            AutosarParameterRef instance
        """
        # TODO: Add validation
        return self._obj
