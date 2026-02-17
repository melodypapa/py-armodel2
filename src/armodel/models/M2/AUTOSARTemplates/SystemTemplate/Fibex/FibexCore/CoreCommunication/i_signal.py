"""ISignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 992)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 227)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # data
        "data_type_policy_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTypePolicyEnum,
        ),  # dataTypePolicyEnum
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # initValue
        "i_signal_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalProps,
        ),  # iSignalProps
        "i_signal_type_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalTypeEnum,
        ),  # iSignalTypeEnum
        "length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # length
        "network": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # network
        "system_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # systemSignal
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # timeout
        "transformation_i_signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (TransformationISignal),
        ),  # transformationISignals
    }

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
