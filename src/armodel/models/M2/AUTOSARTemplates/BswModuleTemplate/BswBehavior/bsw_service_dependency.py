"""BswServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class BswServiceDependency(ServiceDependency):
    """AUTOSAR BswServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_entries: list[RoleBasedBswModuleEntryAssignment]
    ident: Optional[Any]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize BswServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_entries: list[RoleBasedBswModuleEntryAssignment] = []
        self.ident: Optional[Any] = None
        self.service_needs: Optional[ServiceNeeds] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswServiceDependency":
        """Deserialize XML element to BswServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = ARObject._find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_entries (list from container "ASSIGNED-ENTRIES")
        obj.assigned_entries = []
        container = ARObject._find_child_element(element, "ASSIGNED-ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_entries.append(child_value)

        # Parse ident
        child = ARObject._find_child_element(element, "IDENT")
        if child is not None:
            ident_value = child.text
            obj.ident = ident_value

        # Parse service_needs
        child = ARObject._find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = ARObject._deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



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
