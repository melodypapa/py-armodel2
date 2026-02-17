"""InnerDataPrototypeGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 954)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)


class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerDataPrototypeGroupInCompositionInstanceRef."""

    base: Optional[CompositionSwComponentType]
    context_sws: list[Any]
    target_data: Optional[DataPrototypeGroup]
    def __init__(self) -> None:
        """Initialize InnerDataPrototypeGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_data: Optional[DataPrototypeGroup] = None


class InnerDataPrototypeGroupInCompositionInstanceRefBuilder:
    """Builder for InnerDataPrototypeGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerDataPrototypeGroupInCompositionInstanceRef = InnerDataPrototypeGroupInCompositionInstanceRef()

    def build(self) -> InnerDataPrototypeGroupInCompositionInstanceRef:
        """Build and return InnerDataPrototypeGroupInCompositionInstanceRef object.

        Returns:
            InnerDataPrototypeGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
