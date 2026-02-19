"""AutosarParameterRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 317)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
        DataPrototype,
    )



class AutosarParameterRef(ARObject):
    """AUTOSAR AutosarParameterRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    autosar_ref: Optional[ARRef]
    local_parameter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AutosarParameterRef."""
        super().__init__()
        self.autosar_ref: Optional[ARRef] = None
        self.local_parameter_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarParameterRef":
        """Deserialize XML element to AutosarParameterRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarParameterRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse autosar_ref
        child = ARObject._find_child_element(element, "AUTOSAR")
        if child is not None:
            autosar_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.autosar_ref = autosar_ref_value

        # Parse local_parameter_ref
        child = ARObject._find_child_element(element, "LOCAL-PARAMETER")
        if child is not None:
            local_parameter_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.local_parameter_ref = local_parameter_ref_value

        return obj



class AutosarParameterRefBuilder:
    """Builder for AutosarParameterRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarParameterRef = AutosarParameterRef()

    def build(self) -> AutosarParameterRef:
        """Build and return AutosarParameterRef object.

        Returns:
            AutosarParameterRef instance
        """
        # TODO: Add validation
        return self._obj
