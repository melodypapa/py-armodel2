"""PortPrototypeBlueprintInitValue AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Port.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class PortPrototypeBlueprintInitValue(ARObject):
    """AUTOSAR PortPrototypeBlueprintInitValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_ref: ARRef
    value: ValueSpecification
    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprintInitValue."""
        super().__init__()
        self.data_prototype_ref: ARRef = None
        self.value: ValueSpecification = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototypeBlueprintInitValue":
        """Deserialize XML element to PortPrototypeBlueprintInitValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototypeBlueprintInitValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_prototype_ref
        child = ARObject._find_child_element(element, "DATA-PROTOTYPE")
        if child is not None:
            data_prototype_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.data_prototype_ref = data_prototype_ref_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.value = value_value

        return obj



class PortPrototypeBlueprintInitValueBuilder:
    """Builder for PortPrototypeBlueprintInitValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprintInitValue = PortPrototypeBlueprintInitValue()

    def build(self) -> PortPrototypeBlueprintInitValue:
        """Build and return PortPrototypeBlueprintInitValue object.

        Returns:
            PortPrototypeBlueprintInitValue instance
        """
        # TODO: Add validation
        return self._obj
