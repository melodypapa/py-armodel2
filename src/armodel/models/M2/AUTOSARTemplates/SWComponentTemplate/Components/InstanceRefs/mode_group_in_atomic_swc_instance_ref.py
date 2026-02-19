"""ModeGroupInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 961)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from abc import ABC, abstractmethod


class ModeGroupInAtomicSwcInstanceRef(ARObject, ABC):
    """AUTOSAR ModeGroupInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[AtomicSwComponentType]
    context_port_ref: Optional[ARRef]
    target_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeGroupInAtomicSwcInstanceRef":
        """Deserialize XML element to ModeGroupInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeGroupInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "AtomicSwComponentType")
            obj.base = base_value

        # Parse context_port_ref
        child = ARObject._find_child_element(element, "CONTEXT-PORT")
        if child is not None:
            context_port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.context_port_ref = context_port_ref_value

        # Parse target_ref
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.target_ref = target_ref_value

        return obj



class ModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for ModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeGroupInAtomicSwcInstanceRef = ModeGroupInAtomicSwcInstanceRef()

    def build(self) -> ModeGroupInAtomicSwcInstanceRef:
        """Build and return ModeGroupInAtomicSwcInstanceRef object.

        Returns:
            ModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
