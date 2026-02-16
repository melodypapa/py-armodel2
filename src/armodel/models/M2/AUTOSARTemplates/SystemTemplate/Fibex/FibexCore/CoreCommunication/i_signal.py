"""ISignal AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
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
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ISignal(FibexElement):
    """AUTOSAR ISignal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data", None, False, False, DataTransformation),  # data
        ("data_type_policy_enum", None, False, False, DataTypePolicyEnum),  # dataTypePolicyEnum
        ("init_value", None, False, False, ValueSpecification),  # initValue
        ("i_signal_props", None, False, False, ISignalProps),  # iSignalProps
        ("i_signal_type_enum", None, False, False, ISignalTypeEnum),  # iSignalTypeEnum
        ("length", None, True, False, None),  # length
        ("network", None, False, False, SwDataDefProps),  # network
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
        ("timeout", None, False, False, ValueSpecification),  # timeout
        ("transformation_i_signals", None, False, True, any (TransformationISignal)),  # transformationISignals
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignal to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignal":
        """Create ISignal from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignal instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignal since parent returns ARObject
        return cast("ISignal", obj)


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
