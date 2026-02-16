"""SwDataDefProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_pointer_target_props import (
    SwPointerTargetProps,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_text_props import (
    SwTextProps,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class SwDataDefProps(ARObject):
    """AUTOSAR SwDataDefProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("additional_native", None, True, False, None),  # additionalNative
        ("annotations", None, False, True, Annotation),  # annotations
        ("base_type", None, False, False, SwBaseType),  # baseType
        ("compu_method", None, False, False, CompuMethod),  # compuMethod
        ("data_constr", None, False, False, DataConstr),  # dataConstr
        ("display_format_string", None, True, False, None),  # displayFormatString
        ("display", None, False, False, DisplayPresentationEnum),  # display
        ("implementation", None, False, False, AbstractImplementationDataType),  # implementation
        ("invalid_value", None, False, False, ValueSpecification),  # invalidValue
        ("step_size", None, True, False, None),  # stepSize
        ("sw_addr_method", None, False, False, SwAddrMethod),  # swAddrMethod
        ("sw_alignment", None, True, False, None),  # swAlignment
        ("sw_bit", None, False, False, SwBitRepresentation),  # swBit
        ("sw_calibration_access", None, False, False, SwCalibrationAccessEnum),  # swCalibrationAccess
        ("sw_calprm_axis_set", None, False, False, SwCalprmAxisSet),  # swCalprmAxisSet
        ("sw_comparisons", None, False, True, SwVariableRefProxy),  # swComparisons
        ("sw_data", None, False, False, SwDataDependency),  # swData
        ("sw_host_variable", None, False, False, SwVariableRefProxy),  # swHostVariable
        ("sw_impl_policy_enum", None, False, False, SwImplPolicyEnum),  # swImplPolicyEnum
        ("sw_intended", None, True, False, None),  # swIntended
        ("sw_interpolation", None, True, False, None),  # swInterpolation
        ("sw_is_virtual", None, True, False, None),  # swIsVirtual
        ("sw_pointer_target_props", None, False, False, SwPointerTargetProps),  # swPointerTargetProps
        ("sw_record", None, False, False, SwRecordLayout),  # swRecord
        ("sw_refresh", None, False, False, MultidimensionalTime),  # swRefresh
        ("sw_text_props", None, False, False, SwTextProps),  # swTextProps
        ("sw_value_blocks", None, False, True, None),  # swValueBlocks
        ("unit", None, False, False, Unit),  # unit
        ("value_axis_data", None, False, False, ApplicationPrimitiveDataType),  # valueAxisData
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwDataDefProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDefProps":
        """Create SwDataDefProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwDataDefProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwDataDefProps since parent returns ARObject
        return cast("SwDataDefProps", obj)


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
