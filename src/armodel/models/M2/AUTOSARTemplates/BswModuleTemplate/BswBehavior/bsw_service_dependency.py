"""BswServiceDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class BswServiceDependency(ServiceDependency):
    """AUTOSAR BswServiceDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_datas", None, False, True, any (RoleBasedData)),  # assignedDatas
        ("assigned_entries", None, False, True, RoleBasedBswModuleEntryAssignment),  # assignedEntries
        ("ident", None, False, False, any (BswService)),  # ident
        ("service_needs", None, False, False, ServiceNeeds),  # serviceNeeds
    ]

    def __init__(self) -> None:
        """Initialize BswServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_entries: list[RoleBasedBswModuleEntryAssignment] = []
        self.ident: Optional[Any] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswServiceDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswServiceDependency":
        """Create BswServiceDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswServiceDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswServiceDependency since parent returns ARObject
        return cast("BswServiceDependency", obj)


class BswServiceDependencyBuilder:
    """Builder for BswServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswServiceDependency = BswServiceDependency()

    def build(self) -> BswServiceDependency:
        """Build and return BswServiceDependency object.

        Returns:
            BswServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
