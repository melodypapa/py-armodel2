"""SwDataDefProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 339)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 46)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2062)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 31)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 467)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 34)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    DisplayPresentationEnum,
    SwCalibrationAccessEnum,
    SwImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    Boolean,
    DisplayFormatString,
    Float,
    Identifier,
    NativeDeclarationString,
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
    ApplicationPrimitiveDataType,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_bit_representation import (
    SwBitRepresentation,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_set import (
    SwCalprmAxisSet,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_dependency import (
    SwDataDependency,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_text_props import (
    SwTextProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_pointer_target_props import (
        SwPointerTargetProps,
    )
    from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
        SwVariableRefProxy,
    )



class SwDataDefProps(ARObject):
    """AUTOSAR SwDataDefProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "additional_native": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # additionalNative
        "annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Annotation,
        ),  # annotations
        "base_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwBaseType,
        ),  # baseType
        "compu_method": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuMethod,
        ),  # compuMethod
        "data_constr": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataConstr,
        ),  # dataConstr
        "display_format_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # displayFormatString
        "display": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DisplayPresentationEnum,
        ),  # display
        "implementation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractImplementationDataType,
        ),  # implementation
        "invalid_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # invalidValue
        "step_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # stepSize
        "sw_addr_method": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwAddrMethod,
        ),  # swAddrMethod
        "sw_alignment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swAlignment
        "sw_bit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwBitRepresentation,
        ),  # swBit
        "sw_calibration_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalibrationAccessEnum,
        ),  # swCalibrationAccess
        "sw_calprm_axis_set": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalprmAxisSet,
        ),  # swCalprmAxisSet
        "sw_comparisons": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="SwVariableRefProxy",
        ),  # swComparisons
        "sw_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDependency,
        ),  # swData
        "sw_host_variable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="SwVariableRefProxy",
        ),  # swHostVariable
        "sw_impl_policy_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwImplPolicyEnum,
        ),  # swImplPolicyEnum
        "sw_intended": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swIntended
        "sw_interpolation": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swInterpolation
        "sw_is_virtual": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swIsVirtual
        "sw_pointer_target_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="SwPointerTargetProps",
        ),  # swPointerTargetProps
        "sw_record": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwRecordLayout,
        ),  # swRecord
        "sw_refresh": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # swRefresh
        "sw_text_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwTextProps,
        ),  # swTextProps
        "sw_value_blocks": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # swValueBlocks
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
        "value_axis_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationPrimitiveDataType,
        ),  # valueAxisData
    }

    def __init__(self) -> None:
        """Initialize SwDataDefProps."""
        super().__init__()
        self.additional_native: Optional[NativeDeclarationString] = None
        self.annotations: list[Annotation] = []
        self.base_type: Optional[SwBaseType] = None
        self.compu_method: Optional[CompuMethod] = None
        self.data_constr: Optional[DataConstr] = None
        self.display_format_string: Optional[DisplayFormatString] = None
        self.display: Optional[DisplayPresentationEnum] = None
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.invalid_value: Optional[ValueSpecification] = None
        self.step_size: Optional[Float] = None
        self.sw_addr_method: Optional[SwAddrMethod] = None
        self.sw_alignment: Optional[AlignmentType] = None
        self.sw_bit: Optional[SwBitRepresentation] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis_set: Optional[SwCalprmAxisSet] = None
        self.sw_comparisons: list[SwVariableRefProxy] = []
        self.sw_data: Optional[SwDataDependency] = None
        self.sw_host_variable: Optional[SwVariableRefProxy] = None
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.sw_intended: Optional[Numerical] = None
        self.sw_interpolation: Optional[Identifier] = None
        self.sw_is_virtual: Optional[Boolean] = None
        self.sw_pointer_target_props: Optional[SwPointerTargetProps] = None
        self.sw_record: Optional[SwRecordLayout] = None
        self.sw_refresh: Optional[MultidimensionalTime] = None
        self.sw_text_props: Optional[SwTextProps] = None
        self.sw_value_blocks: list[Numerical] = []
        self.unit: Optional[Unit] = None
        self.value_axis_data: Optional[ApplicationPrimitiveDataType] = None


class SwDataDefPropsBuilder:
    """Builder for SwDataDefProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDefProps = SwDataDefProps()

    def build(self) -> SwDataDefProps:
        """Build and return SwDataDefProps object.

        Returns:
            SwDataDefProps instance
        """
        # TODO: Add validation
        return self._obj
