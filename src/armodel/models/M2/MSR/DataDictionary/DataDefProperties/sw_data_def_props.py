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

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
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

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_pointer_target_props import (
        SwPointerTargetProps,
    )
    from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
        SwVariableRefProxy,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class SwDataDefProps(ARObject):
    """AUTOSAR SwDataDefProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional_native_type_qualifier: Optional[NativeDeclarationString]
    annotations: list[Annotation]
    base_type: Optional[SwBaseType]
    compu_method: Optional[CompuMethod]
    data_constr: Optional[DataConstr]
    display_format: Optional[DisplayFormatString]
    display_presentation: Optional[DisplayPresentationEnum]
    implementation_data_type: Optional[AbstractImplementationDataType]
    invalid_value: Optional[ValueSpecification]
    step_size: Optional[Float]
    sw_addr_method: Optional[SwAddrMethod]
    sw_alignment: Optional[AlignmentType]
    sw_bit_representation: Optional[SwBitRepresentation]
    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    sw_calprm_axis_set_ref: Optional[ARRef]
    sw_comparison_variable_refs: list[ARRef]
    sw_data_dependency_ref: Optional[ARRef]
    sw_host_variable_ref: Optional[ARRef]
    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    sw_intended_resolution: Optional[Numerical]
    sw_interpolation_method: Optional[Identifier]
    sw_is_virtual: Optional[Boolean]
    sw_pointer_target_props: Optional[SwPointerTargetProps]
    sw_record_layout: Optional[SwRecordLayout]
    sw_refresh_timing: Optional[MultidimensionalTime]
    sw_text_props: Optional[SwTextProps]
    sw_value_block_size: Optional[Numerical]
    sw_value_block_size_mults: list[Numerical]
    unit: Optional[Unit]
    value_axis_data_type: Optional[ApplicationPrimitiveDataType]
    def __init__(self) -> None:
        """Initialize SwDataDefProps."""
        super().__init__()
        self.additional_native_type_qualifier: Optional[NativeDeclarationString] = None
        self.annotations: list[Annotation] = []
        self.base_type: Optional[SwBaseType] = None
        self.compu_method: Optional[CompuMethod] = None
        self.data_constr: Optional[DataConstr] = None
        self.display_format: Optional[DisplayFormatString] = None
        self.display_presentation: Optional[DisplayPresentationEnum] = None
        self.implementation_data_type: Optional[AbstractImplementationDataType] = None
        self.invalid_value: Optional[ValueSpecification] = None
        self.step_size: Optional[Float] = None
        self.sw_addr_method: Optional[SwAddrMethod] = None
        self.sw_alignment: Optional[AlignmentType] = None
        self.sw_bit_representation: Optional[SwBitRepresentation] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis_set_ref: Optional[ARRef] = None
        self.sw_comparison_variable_refs: list[ARRef] = []
        self.sw_data_dependency_ref: Optional[ARRef] = None
        self.sw_host_variable_ref: Optional[ARRef] = None
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.sw_intended_resolution: Optional[Numerical] = None
        self.sw_interpolation_method: Optional[Identifier] = None
        self.sw_is_virtual: Optional[Boolean] = None
        self.sw_pointer_target_props: Optional[SwPointerTargetProps] = None
        self.sw_record_layout: Optional[SwRecordLayout] = None
        self.sw_refresh_timing: Optional[MultidimensionalTime] = None
        self.sw_text_props: Optional[SwTextProps] = None
        self.sw_value_block_size: Optional[Numerical] = None
        self.sw_value_block_size_mults: list[Numerical] = []
        self.unit: Optional[Unit] = None
        self.value_axis_data_type: Optional[ApplicationPrimitiveDataType] = None


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
