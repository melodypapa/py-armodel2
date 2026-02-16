"""PerInstanceMemory AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    String,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class PerInstanceMemory(Identifiable):
    """AUTOSAR PerInstanceMemory."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, True, False, None),  # initValue
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
        ("type", None, True, False, None),  # type
        ("type_definition", None, True, False, None),  # typeDefinition
    ]

    def __init__(self) -> None:
        """Initialize PerInstanceMemory."""
        super().__init__()
        self.init_value: Optional[String] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.type: Optional[CIdentifier] = None
        self.type_definition: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PerInstanceMemory to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemory":
        """Create PerInstanceMemory from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PerInstanceMemory instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PerInstanceMemory since parent returns ARObject
        return cast("PerInstanceMemory", obj)


class PerInstanceMemoryBuilder:
    """Builder for PerInstanceMemory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemory = PerInstanceMemory()

    def build(self) -> PerInstanceMemory:
        """Build and return PerInstanceMemory object.

        Returns:
            PerInstanceMemory instance
        """
        # TODO: Add validation
        return self._obj
