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
    i_signal_group: Optional[ISignalGroup]
    packing_byte: Optional[ByteOrderEnum]
    start_position: Optional[UnlimitedInteger]
    transfer_property_enum: Optional[TransferPropertyEnum]
    update: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize ISignalToIPduMapping."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group: Optional[ISignalGroup] = None
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.start_position: Optional[UnlimitedInteger] = None
        self.transfer_property_enum: Optional[TransferPropertyEnum] = None
        self.update: Optional[UnlimitedInteger] = None


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
