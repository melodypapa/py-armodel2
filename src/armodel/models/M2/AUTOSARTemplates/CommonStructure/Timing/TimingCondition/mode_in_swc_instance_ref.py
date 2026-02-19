"""ModeInSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class ModeInSwcInstanceRef(ARObject):
    """AUTOSAR ModeInSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[SwComponentType]
    contexts: list[Any]
    context_mode_ref: Optional[ARRef]
    context_port_ref: Optional[ARRef]
    target_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeInSwcInstanceRef."""
        super().__init__()
        self.base: Optional[SwComponentType] = None
        self.contexts: list[Any] = []
        self.context_mode_ref: Optional[ARRef] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_mode: Optional[ModeDeclaration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInSwcInstanceRef":
        """Deserialize XML element to ModeInSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "SwComponentType")
            obj.base = base_value

        # Parse contexts (list)
        obj.contexts = []
        for child in ARObject._find_all_child_elements(element, "CONTEXTS"):
            contexts_value = child.text
            obj.contexts.append(contexts_value)

        # Parse context_mode_ref
        child = ARObject._find_child_element(element, "CONTEXT-MODE")
        if child is not None:
            context_mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.context_mode_ref = context_mode_ref_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT")
        if child is not None:
            context_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.context_port_ref = context_port_ref_value

        # Parse target_mode
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.target_mode = target_mode_value

        return obj



class ModeInSwcInstanceRefBuilder:
    """Builder for ModeInSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInSwcInstanceRef = ModeInSwcInstanceRef()

    def build(self) -> ModeInSwcInstanceRef:
        """Build and return ModeInSwcInstanceRef object.

        Returns:
            ModeInSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
