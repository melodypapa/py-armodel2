"""BinaryManifestResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 915)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from abc import ABC, abstractmethod


class BinaryManifestResource(Identifiable, ABC):
    """AUTOSAR BinaryManifestResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    global_resource: Optional[PositiveInteger]
    resource: Optional[Any]
    resource_guard: Optional[String]
    def __init__(self) -> None:
        """Initialize BinaryManifestResource."""
        super().__init__()
        self.global_resource: Optional[PositiveInteger] = None
        self.resource: Optional[Any] = None
        self.resource_guard: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResource":
        """Deserialize XML element to BinaryManifestResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestResource object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse global_resource
        child = ARObject._find_child_element(element, "GLOBAL-RESOURCE")
        if child is not None:
            global_resource_value = child.text
            obj.global_resource = global_resource_value

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = child.text
            obj.resource = resource_value

        # Parse resource_guard
        child = ARObject._find_child_element(element, "RESOURCE-GUARD")
        if child is not None:
            resource_guard_value = child.text
            obj.resource_guard = resource_guard_value

        return obj



class BinaryManifestResourceBuilder:
    """Builder for BinaryManifestResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResource = BinaryManifestResource()

    def build(self) -> BinaryManifestResource:
        """Build and return BinaryManifestResource object.

        Returns:
            BinaryManifestResource instance
        """
        # TODO: Add validation
        return self._obj
