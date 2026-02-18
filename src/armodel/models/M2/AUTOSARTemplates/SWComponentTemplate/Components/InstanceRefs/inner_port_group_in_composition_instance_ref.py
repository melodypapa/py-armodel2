"""InnerPortGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class InnerPortGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerPortGroupInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    contexts: list[Any]
    target_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InnerPortGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.contexts: list[Any] = []
        self.target_ref: Optional[ARRef] = None


class InnerPortGroupInCompositionInstanceRefBuilder:
    """Builder for InnerPortGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerPortGroupInCompositionInstanceRef = InnerPortGroupInCompositionInstanceRef()

    def build(self) -> InnerPortGroupInCompositionInstanceRef:
        """Build and return InnerPortGroupInCompositionInstanceRef object.

        Returns:
            InnerPortGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
