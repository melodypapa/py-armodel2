"""DiagnosticMemoryDestinationUserDefined AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)


class DiagnosticMemoryDestinationUserDefined(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationUserDefined."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auth_roles: list[DiagnosticAuthRole]
    memory_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationUserDefined."""
        super().__init__()
        self.auth_roles: list[DiagnosticAuthRole] = []
        self.memory_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestinationUserDefined":
        """Deserialize XML element to DiagnosticMemoryDestinationUserDefined object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestinationUserDefined object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestinationUserDefined, cls).deserialize(element)

        # Parse auth_roles (list from container "AUTH-ROLES")
        obj.auth_roles = []
        container = ARObject._find_child_element(element, "AUTH-ROLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.auth_roles.append(child_value)

        # Parse memory_id
        child = ARObject._find_child_element(element, "MEMORY-ID")
        if child is not None:
            memory_id_value = child.text
            obj.memory_id = memory_id_value

        return obj



class DiagnosticMemoryDestinationUserDefinedBuilder:
    """Builder for DiagnosticMemoryDestinationUserDefined."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationUserDefined = DiagnosticMemoryDestinationUserDefined()

    def build(self) -> DiagnosticMemoryDestinationUserDefined:
        """Build and return DiagnosticMemoryDestinationUserDefined object.

        Returns:
            DiagnosticMemoryDestinationUserDefined instance
        """
        # TODO: Add validation
        return self._obj
