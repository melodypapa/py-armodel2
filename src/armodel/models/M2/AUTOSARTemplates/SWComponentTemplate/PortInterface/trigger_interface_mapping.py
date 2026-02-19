"""TriggerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger_mapping import (
    TriggerMapping,
)


class TriggerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR TriggerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerInterfaceMapping."""
        super().__init__()
        self.trigger_mapping_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerInterfaceMapping":
        """Deserialize XML element to TriggerInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerInterfaceMapping, cls).deserialize(element)

        # Parse trigger_mapping_refs (list from container "TRIGGER-MAPPINGS")
        obj.trigger_mapping_refs = []
        container = ARObject._find_child_element(element, "TRIGGER-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_mapping_refs.append(child_value)

        return obj



class TriggerInterfaceMappingBuilder:
    """Builder for TriggerInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterfaceMapping = TriggerInterfaceMapping()

    def build(self) -> TriggerInterfaceMapping:
        """Build and return TriggerInterfaceMapping object.

        Returns:
            TriggerInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
