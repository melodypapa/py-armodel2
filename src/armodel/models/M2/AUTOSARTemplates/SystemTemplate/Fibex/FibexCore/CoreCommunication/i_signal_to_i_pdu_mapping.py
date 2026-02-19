"""ISignalToIPduMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 325)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    TransferPropertyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)


class ISignalToIPduMapping(Identifiable):
    """AUTOSAR ISignalToIPduMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal: Optional[ISignal]
    i_signal_group_ref: Optional[ARRef]
    packing_byte: Optional[ByteOrderEnum]
    start_position: Optional[UnlimitedInteger]
    transfer_property_enum: Optional[TransferPropertyEnum]
    update: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize ISignalToIPduMapping."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.start_position: Optional[UnlimitedInteger] = None
        self.transfer_property_enum: Optional[TransferPropertyEnum] = None
        self.update: Optional[UnlimitedInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalToIPduMapping":
        """Deserialize XML element to ISignalToIPduMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalToIPduMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse i_signal
        child = ARObject._find_child_element(element, "I-SIGNAL")
        if child is not None:
            i_signal_value = ARObject._deserialize_by_tag(child, "ISignal")
            obj.i_signal = i_signal_value

        # Parse i_signal_group_ref
        child = ARObject._find_child_element(element, "I-SIGNAL-GROUP")
        if child is not None:
            i_signal_group_ref_value = ARObject._deserialize_by_tag(child, "ISignalGroup")
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse packing_byte
        child = ARObject._find_child_element(element, "PACKING-BYTE")
        if child is not None:
            packing_byte_value = child.text
            obj.packing_byte = packing_byte_value

        # Parse start_position
        child = ARObject._find_child_element(element, "START-POSITION")
        if child is not None:
            start_position_value = child.text
            obj.start_position = start_position_value

        # Parse transfer_property_enum
        child = ARObject._find_child_element(element, "TRANSFER-PROPERTY-ENUM")
        if child is not None:
            transfer_property_enum_value = child.text
            obj.transfer_property_enum = transfer_property_enum_value

        # Parse update
        child = ARObject._find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



class ISignalToIPduMappingBuilder:
    """Builder for ISignalToIPduMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalToIPduMapping = ISignalToIPduMapping()

    def build(self) -> ISignalToIPduMapping:
        """Build and return ISignalToIPduMapping object.

        Returns:
            ISignalToIPduMapping instance
        """
        # TODO: Add validation
        return self._obj
