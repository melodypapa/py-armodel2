"""ISignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 993)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)


class ISignalGroup(FibexElement):
    """AUTOSAR ISignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    com_based: Optional[DataTransformation]
    i_signals: list[ISignal]
    system_signal_group_ref: Optional[ARRef]
    transformation_i_signals: list[Any]
    def __init__(self) -> None:
        """Initialize ISignalGroup."""
        super().__init__()
        self.com_based: Optional[DataTransformation] = None
        self.i_signals: list[ISignal] = []
        self.system_signal_group_ref: Optional[ARRef] = None
        self.transformation_i_signals: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalGroup":
        """Deserialize XML element to ISignalGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse com_based
        child = ARObject._find_child_element(element, "COM-BASED")
        if child is not None:
            com_based_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.com_based = com_based_value

        # Parse i_signals (list)
        obj.i_signals = []
        for child in ARObject._find_all_child_elements(element, "I-SIGNALS"):
            i_signals_value = ARObject._deserialize_by_tag(child, "ISignal")
            obj.i_signals.append(i_signals_value)

        # Parse system_signal_group_ref
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL-GROUP")
        if child is not None:
            system_signal_group_ref_value = ARObject._deserialize_by_tag(child, "SystemSignalGroup")
            obj.system_signal_group_ref = system_signal_group_ref_value

        # Parse transformation_i_signals (list)
        obj.transformation_i_signals = []
        for child in ARObject._find_all_child_elements(element, "TRANSFORMATION-I-SIGNALS"):
            transformation_i_signals_value = child.text
            obj.transformation_i_signals.append(transformation_i_signals_value)

        return obj



class ISignalGroupBuilder:
    """Builder for ISignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalGroup = ISignalGroup()

    def build(self) -> ISignalGroup:
        """Build and return ISignalGroup object.

        Returns:
            ISignalGroup instance
        """
        # TODO: Add validation
        return self._obj
