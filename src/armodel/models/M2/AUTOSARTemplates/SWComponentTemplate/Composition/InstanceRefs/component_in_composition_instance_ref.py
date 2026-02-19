"""ComponentInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 950)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 219)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ComponentInCompositionInstanceRef(ARObject):
    """AUTOSAR ComponentInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    contexts: list[Any]
    target: Optional[Any]
    def __init__(self) -> None:
        """Initialize ComponentInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.contexts: list[Any] = []
        self.target: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentInCompositionInstanceRef":
        """Deserialize XML element to ComponentInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComponentInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = child.text
            obj.target = target_value

        return obj



class ComponentInCompositionInstanceRefBuilder:
    """Builder for ComponentInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentInCompositionInstanceRef = ComponentInCompositionInstanceRef()

    def build(self) -> ComponentInCompositionInstanceRef:
        """Build and return ComponentInCompositionInstanceRef object.

        Returns:
            ComponentInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
