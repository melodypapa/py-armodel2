"""CpSoftwareClusterResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 271)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)
from abc import ABC, abstractmethod


class CpSoftwareClusterResource(Identifiable, ABC):
    """AUTOSAR CpSoftwareClusterResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dependents: list[RoleBasedResourceDependency]
    global_resource: Optional[PositiveInteger]
    is_mandatory: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResource."""
        super().__init__()
        self.dependents: list[RoleBasedResourceDependency] = []
        self.global_resource: Optional[PositiveInteger] = None
        self.is_mandatory: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResource":
        """Deserialize XML element to CpSoftwareClusterResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResource object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dependents (list)
        obj.dependents = []
        for child in ARObject._find_all_child_elements(element, "DEPENDENTS"):
            dependents_value = ARObject._deserialize_by_tag(child, "RoleBasedResourceDependency")
            obj.dependents.append(dependents_value)

        # Parse global_resource
        child = ARObject._find_child_element(element, "GLOBAL-RESOURCE")
        if child is not None:
            global_resource_value = child.text
            obj.global_resource = global_resource_value

        # Parse is_mandatory
        child = ARObject._find_child_element(element, "IS-MANDATORY")
        if child is not None:
            is_mandatory_value = child.text
            obj.is_mandatory = is_mandatory_value

        return obj



class CpSoftwareClusterResourceBuilder:
    """Builder for CpSoftwareClusterResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResource = CpSoftwareClusterResource()

    def build(self) -> CpSoftwareClusterResource:
        """Build and return CpSoftwareClusterResource object.

        Returns:
            CpSoftwareClusterResource instance
        """
        # TODO: Add validation
        return self._obj
