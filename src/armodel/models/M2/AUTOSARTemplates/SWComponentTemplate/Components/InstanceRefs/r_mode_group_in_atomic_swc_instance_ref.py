"""RModeGroupInAtomicSWCInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 948)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR RModeGroupInAtomicSWCInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype: Optional[AbstractRequiredPortPrototype]
    target_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RModeGroupInAtomicSWCInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_mode_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RModeGroupInAtomicSWCInstanceRef":
        """Deserialize XML element to RModeGroupInAtomicSWCInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RModeGroupInAtomicSWCInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RModeGroupInAtomicSWCInstanceRef, cls).deserialize(element)

        # Parse context_r_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE")
        if child is not None:
            context_r_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.context_r_port_prototype = context_r_port_prototype_value

        # Parse target_mode_ref
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.target_mode_ref = target_mode_ref_value

        return obj



class RModeGroupInAtomicSWCInstanceRefBuilder:
    """Builder for RModeGroupInAtomicSWCInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RModeGroupInAtomicSWCInstanceRef = RModeGroupInAtomicSWCInstanceRef()

    def build(self) -> RModeGroupInAtomicSWCInstanceRef:
        """Build and return RModeGroupInAtomicSWCInstanceRef object.

        Returns:
            RModeGroupInAtomicSWCInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
