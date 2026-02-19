"""DataReceiveErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataReceiveErrorEvent(RTEEvent):
    """AUTOSAR DataReceiveErrorEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataReceiveErrorEvent."""
        super().__init__()
        self.data_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataReceiveErrorEvent":
        """Deserialize XML element to DataReceiveErrorEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataReceiveErrorEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_ref
        child = ARObject._find_child_element(element, "DATA")
        if child is not None:
            data_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.data_ref = data_ref_value

        return obj



class DataReceiveErrorEventBuilder:
    """Builder for DataReceiveErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataReceiveErrorEvent = DataReceiveErrorEvent()

    def build(self) -> DataReceiveErrorEvent:
        """Build and return DataReceiveErrorEvent object.

        Returns:
            DataReceiveErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
