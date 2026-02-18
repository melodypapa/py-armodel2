"""InnerRunnableEntityGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 956)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class InnerRunnableEntityGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerRunnableEntityGroupInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    context_sws: list[Any]
    target_runnable_ref: ARRef
    def __init__(self) -> None:
        """Initialize InnerRunnableEntityGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_runnable_ref: ARRef = None


class InnerRunnableEntityGroupInCompositionInstanceRefBuilder:
    """Builder for InnerRunnableEntityGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerRunnableEntityGroupInCompositionInstanceRef = InnerRunnableEntityGroupInCompositionInstanceRef()

    def build(self) -> InnerRunnableEntityGroupInCompositionInstanceRef:
        """Build and return InnerRunnableEntityGroupInCompositionInstanceRef object.

        Returns:
            InnerRunnableEntityGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
