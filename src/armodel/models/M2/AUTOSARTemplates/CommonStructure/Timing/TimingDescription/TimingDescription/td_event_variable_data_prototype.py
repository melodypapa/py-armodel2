"""TDEventVariableDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class TDEventVariableDataPrototype(TDEventVfbPort):
    """AUTOSAR TDEventVariableDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_ref: Optional[ARRef]
    td_event_variable_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventVariableDataPrototype."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.td_event_variable_type: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVariableDataPrototype":
        """Deserialize XML element to TDEventVariableDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVariableDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventVariableDataPrototype, cls).deserialize(element)

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse td_event_variable_type
        child = ARObject._find_child_element(element, "TD-EVENT-VARIABLE-TYPE")
        if child is not None:
            td_event_variable_type_value = child.text
            obj.td_event_variable_type = td_event_variable_type_value

        return obj



class TDEventVariableDataPrototypeBuilder:
    """Builder for TDEventVariableDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVariableDataPrototype = TDEventVariableDataPrototype()

    def build(self) -> TDEventVariableDataPrototype:
        """Build and return TDEventVariableDataPrototype object.

        Returns:
            TDEventVariableDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
