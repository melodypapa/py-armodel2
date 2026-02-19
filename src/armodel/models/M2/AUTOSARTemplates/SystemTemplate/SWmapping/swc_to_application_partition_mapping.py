"""SwcToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class SwcToApplicationPartitionMapping(Identifiable):
    """AUTOSAR SwcToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[ApplicationPartition]
    sw_component_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.sw_component_prototype_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToApplicationPartitionMapping":
        """Deserialize XML element to SwcToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToApplicationPartitionMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse application
        child = ARObject._find_child_element(element, "APPLICATION")
        if child is not None:
            application_value = ARObject._deserialize_by_tag(child, "ApplicationPartition")
            obj.application = application_value

        # Parse sw_component_prototype_ref
        child = ARObject._find_child_element(element, "SW-COMPONENT-PROTOTYPE")
        if child is not None:
            sw_component_prototype_ref_value = ARObject._deserialize_by_tag(child, "SwComponentPrototype")
            obj.sw_component_prototype_ref = sw_component_prototype_ref_value

        return obj



class SwcToApplicationPartitionMappingBuilder:
    """Builder for SwcToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToApplicationPartitionMapping = SwcToApplicationPartitionMapping()

    def build(self) -> SwcToApplicationPartitionMapping:
        """Build and return SwcToApplicationPartitionMapping object.

        Returns:
            SwcToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
