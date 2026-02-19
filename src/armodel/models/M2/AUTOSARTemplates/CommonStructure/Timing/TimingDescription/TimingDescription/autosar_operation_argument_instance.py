"""AutosarOperationArgumentInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class AutosarOperationArgumentInstance(Identifiable):
    """AUTOSAR AutosarOperationArgumentInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AutosarOperationArgumentInstance."""
        super().__init__()
        self.operation_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarOperationArgumentInstance":
        """Deserialize XML element to AutosarOperationArgumentInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarOperationArgumentInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AutosarOperationArgumentInstance, cls).deserialize(element)

        # Parse operation_ref
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.operation_ref = operation_ref_value

        return obj



class AutosarOperationArgumentInstanceBuilder:
    """Builder for AutosarOperationArgumentInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarOperationArgumentInstance = AutosarOperationArgumentInstance()

    def build(self) -> AutosarOperationArgumentInstance:
        """Build and return AutosarOperationArgumentInstance object.

        Returns:
            AutosarOperationArgumentInstance instance
        """
        # TODO: Add validation
        return self._obj
