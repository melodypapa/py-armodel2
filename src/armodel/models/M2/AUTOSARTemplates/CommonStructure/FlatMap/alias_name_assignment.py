"""AliasNameAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("flat_instance", None, False, False, FlatInstanceDescriptor),  # flatInstance
        ("identifiable", None, False, False, Identifiable),  # identifiable
        ("label", None, False, False, MultilanguageLongName),  # label
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance: Optional[FlatInstanceDescriptor] = None
        self.identifiable: Optional[Identifiable] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AliasNameAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameAssignment":
        """Create AliasNameAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AliasNameAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AliasNameAssignment since parent returns ARObject
        return cast("AliasNameAssignment", obj)


class AliasNameAssignmentBuilder:
    """Builder for AliasNameAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameAssignment = AliasNameAssignment()

    def build(self) -> AliasNameAssignment:
        """Build and return AliasNameAssignment object.

        Returns:
            AliasNameAssignment instance
        """
        # TODO: Add validation
        return self._obj
