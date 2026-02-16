"""BswModuleClientServerEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("encapsulated", None, False, False, BswModuleEntry),  # encapsulated
        ("is_reentrant", None, True, False, None),  # isReentrant
        ("is_synchronous", None, True, False, None),  # isSynchronous
    ]

    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated: Optional[BswModuleEntry] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleClientServerEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleClientServerEntry":
        """Create BswModuleClientServerEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleClientServerEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleClientServerEntry since parent returns ARObject
        return cast("BswModuleClientServerEntry", obj)


class BswModuleClientServerEntryBuilder:
    """Builder for BswModuleClientServerEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()

    def build(self) -> BswModuleClientServerEntry:
        """Build and return BswModuleClientServerEntry object.

        Returns:
            BswModuleClientServerEntry instance
        """
        # TODO: Add validation
        return self._obj
