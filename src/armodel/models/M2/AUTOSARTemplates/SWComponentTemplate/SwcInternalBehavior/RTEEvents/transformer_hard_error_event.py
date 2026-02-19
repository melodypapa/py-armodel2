"""TransformerHardErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TransformerHardErrorEvent(RTEEvent):
    """AUTOSAR TransformerHardErrorEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation: Optional[ClientServerOperation]
    required_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TransformerHardErrorEvent."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.required_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformerHardErrorEvent":
        """Deserialize XML element to TransformerHardErrorEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformerHardErrorEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse required_trigger_ref
        child = ARObject._find_child_element(element, "REQUIRED-TRIGGER")
        if child is not None:
            required_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.required_trigger_ref = required_trigger_ref_value

        return obj



class TransformerHardErrorEventBuilder:
    """Builder for TransformerHardErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformerHardErrorEvent = TransformerHardErrorEvent()

    def build(self) -> TransformerHardErrorEvent:
        """Build and return TransformerHardErrorEvent object.

        Returns:
            TransformerHardErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
