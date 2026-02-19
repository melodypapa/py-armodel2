"""EndToEndProtectionVariablePrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 215)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class EndToEndProtectionVariablePrototype(ARObject):
    """AUTOSAR EndToEndProtectionVariablePrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    receiver_refs: list[ARRef]
    sender_ref: Optional[ARRef]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionVariablePrototype."""
        super().__init__()
        self.receiver_refs: list[ARRef] = []
        self.sender_ref: Optional[ARRef] = None
        self.short_label: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionVariablePrototype":
        """Deserialize XML element to EndToEndProtectionVariablePrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndProtectionVariablePrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse receiver_refs (list from container "RECEIVERS")
        obj.receiver_refs = []
        container = ARObject._find_child_element(element, "RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.receiver_refs.append(child_value)

        # Parse sender_ref
        child = ARObject._find_child_element(element, "SENDER")
        if child is not None:
            sender_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.sender_ref = sender_ref_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class EndToEndProtectionVariablePrototypeBuilder:
    """Builder for EndToEndProtectionVariablePrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionVariablePrototype = EndToEndProtectionVariablePrototype()

    def build(self) -> EndToEndProtectionVariablePrototype:
        """Build and return EndToEndProtectionVariablePrototype object.

        Returns:
            EndToEndProtectionVariablePrototype instance
        """
        # TODO: Add validation
        return self._obj
