"""ISignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 992)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 227)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataTypePolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_props import (
    ISignalProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ISignal(FibexElement):
    """AUTOSAR ISignal."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data: Optional[DataTransformation]
    data_type_policy_enum: Optional[DataTypePolicyEnum]
    init_value: Optional[ValueSpecification]
    i_signal_props: Optional[ISignalProps]
    i_signal_type_enum: Optional[ISignalTypeEnum]
    length: Optional[UnlimitedInteger]
    network: Optional[SwDataDefProps]
    system_signal: Optional[SystemSignal]
    timeout: Optional[ValueSpecification]
    transformation_i_signals: list[Any]
    def __init__(self) -> None:
        """Initialize ISignal."""
        super().__init__()
        self.data: Optional[DataTransformation] = None
        self.data_type_policy_enum: Optional[DataTypePolicyEnum] = None
        self.init_value: Optional[ValueSpecification] = None
        self.i_signal_props: Optional[ISignalProps] = None
        self.i_signal_type_enum: Optional[ISignalTypeEnum] = None
        self.length: Optional[UnlimitedInteger] = None
        self.network: Optional[SwDataDefProps] = None
        self.system_signal: Optional[SystemSignal] = None
        self.timeout: Optional[ValueSpecification] = None
        self.transformation_i_signals: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignal":
        """Deserialize XML element to ISignal object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignal object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignal, cls).deserialize(element)

        # Parse data
        child = ARObject._find_child_element(element, "DATA")
        if child is not None:
            data_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.data = data_value

        # Parse data_type_policy_enum
        child = ARObject._find_child_element(element, "DATA-TYPE-POLICY-ENUM")
        if child is not None:
            data_type_policy_enum_value = DataTypePolicyEnum.deserialize(child)
            obj.data_type_policy_enum = data_type_policy_enum_value

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse i_signal_props
        child = ARObject._find_child_element(element, "I-SIGNAL-PROPS")
        if child is not None:
            i_signal_props_value = ARObject._deserialize_by_tag(child, "ISignalProps")
            obj.i_signal_props = i_signal_props_value

        # Parse i_signal_type_enum
        child = ARObject._find_child_element(element, "I-SIGNAL-TYPE-ENUM")
        if child is not None:
            i_signal_type_enum_value = ISignalTypeEnum.deserialize(child)
            obj.i_signal_type_enum = i_signal_type_enum_value

        # Parse length
        child = ARObject._find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.network = network_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.timeout = timeout_value

        # Parse transformation_i_signals (list from container "TRANSFORMATION-I-SIGNALS")
        obj.transformation_i_signals = []
        container = ARObject._find_child_element(element, "TRANSFORMATION-I-SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_i_signals.append(child_value)

        return obj



class ISignalBuilder:
    """Builder for ISignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignal = ISignal()

    def build(self) -> ISignal:
        """Build and return ISignal object.

        Returns:
            ISignal instance
        """
        # TODO: Add validation
        return self._obj
