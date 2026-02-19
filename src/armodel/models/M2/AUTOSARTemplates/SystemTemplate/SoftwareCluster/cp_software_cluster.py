"""CpSoftwareCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 309)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 893)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class CpSoftwareCluster(ARElement):
    """AUTOSAR CpSoftwareCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    software_cluster: Optional[PositiveInteger]
    sw_components: list[Any]
    sw_composition_component_types: list[CompositionSwComponentType]
    def __init__(self) -> None:
        """Initialize CpSoftwareCluster."""
        super().__init__()
        self.software_cluster: Optional[PositiveInteger] = None
        self.sw_components: list[Any] = []
        self.sw_composition_component_types: list[CompositionSwComponentType] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareCluster":
        """Deserialize XML element to CpSoftwareCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareCluster, cls).deserialize(element)

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = child.text
            obj.software_cluster = software_cluster_value

        # Parse sw_components (list from container "SW-COMPONENTS")
        obj.sw_components = []
        container = ARObject._find_child_element(element, "SW-COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_components.append(child_value)

        # Parse sw_composition_component_types (list from container "SW-COMPOSITION-COMPONENT-TYPES")
        obj.sw_composition_component_types = []
        container = ARObject._find_child_element(element, "SW-COMPOSITION-COMPONENT-TYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_composition_component_types.append(child_value)

        return obj



class CpSoftwareClusterBuilder:
    """Builder for CpSoftwareCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareCluster = CpSoftwareCluster()

    def build(self) -> CpSoftwareCluster:
        """Build and return CpSoftwareCluster object.

        Returns:
            CpSoftwareCluster instance
        """
        # TODO: Add validation
        return self._obj
