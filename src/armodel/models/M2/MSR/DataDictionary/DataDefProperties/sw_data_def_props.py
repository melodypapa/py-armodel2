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
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
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



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
@atp_variant()

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
    base_type_ref: Optional[ARRef]
    compu_method_ref: Optional[ARRef]
    data_constr_ref: Optional[ARRef]
    display_format: Optional[DisplayFormatString]
    display_presentation: Optional[DisplayPresentationEnum]
    implementation_data_type_ref: Optional[ARRef]
    invalid_value: Optional[ValueSpecification]
    step_size: Optional[Float]
    sw_addr_method_ref: Optional[ARRef]
    sw_alignment: Optional[AlignmentType]
    sw_bit_representation: Optional[SwBitRepresentation]
    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    sw_calprm_axis_set: Optional[SwCalprmAxisSet]
    sw_comparison_variables: list[SwVariableRefProxy]
    sw_data_dependency: Optional[SwDataDependency]
    sw_host_variable: Optional[SwVariableRefProxy]
    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    sw_intended_resolution: Optional[Numerical]
    sw_interpolation_method: Optional[Identifier]
    sw_is_virtual: Optional[Boolean]
    sw_pointer_target_props: Optional[SwPointerTargetProps]
    sw_record_layout_ref: Optional[ARRef]
    sw_refresh_timing: Optional[MultidimensionalTime]
    sw_text_props: Optional[SwTextProps]
    sw_value_block_size: Optional[Numerical]
    sw_value_block_size_mults: list[Numerical]
    unit_ref: Optional[ARRef]
    value_axis_data_type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwDataDefProps."""
        super().__init__()
        self.additional_native_type_qualifier: Optional[NativeDeclarationString] = None
        self.annotations: list[Annotation] = []
        self.base_type_ref: Optional[ARRef] = None
        self.compu_method_ref: Optional[ARRef] = None
        self.data_constr_ref: Optional[ARRef] = None
        self.display_format: Optional[DisplayFormatString] = None
        self.display_presentation: Optional[DisplayPresentationEnum] = None
        self.implementation_data_type_ref: Optional[ARRef] = None
        self.invalid_value: Optional[ValueSpecification] = None
        self.step_size: Optional[Float] = None
        self.sw_addr_method_ref: Optional[ARRef] = None
        self.sw_alignment: Optional[AlignmentType] = None
        self.sw_bit_representation: Optional[SwBitRepresentation] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis_set: Optional[SwCalprmAxisSet] = None
        self.sw_comparison_variables: list[SwVariableRefProxy] = []
        self.sw_data_dependency: Optional[SwDataDependency] = None
        self.sw_host_variable: Optional[SwVariableRefProxy] = None
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.sw_intended_resolution: Optional[Numerical] = None
        self.sw_interpolation_method: Optional[Identifier] = None
        self.sw_is_virtual: Optional[Boolean] = None
        self.sw_pointer_target_props: Optional[SwPointerTargetProps] = None
        self.sw_record_layout_ref: Optional[ARRef] = None
        self.sw_refresh_timing: Optional[MultidimensionalTime] = None
        self.sw_text_props: Optional[SwTextProps] = None
        self.sw_value_block_size: Optional[Numerical] = None
        self.sw_value_block_size_mults: list[Numerical] = []
        self.unit_ref: Optional[ARRef] = None
        self.value_axis_data_type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDefProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwDataDefProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize additional_native_type_qualifier
        if self.additional_native_type_qualifier is not None:
            serialized = SerializationHelper.serialize_item(self.additional_native_type_qualifier, "NativeDeclarationString")
            if serialized is not None:
                wrapped = ET.Element("ADDITIONAL-NATIVE-TYPE-QUALIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize annotations (list from container "ANNOTATIONS")
        if self.annotations:
            container = ET.Element("ANNOTATIONS")
            for item in self.annotations:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("Annotation", package_data):
                    # Simple primitive type
                    child = ET.Element("ANNOTATION")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("Annotation", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize base_type_ref
        if self.base_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_ref, "SwBaseType")
            if serialized is not None:
                wrapped = ET.Element("BASE-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize compu_method_ref
        if self.compu_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.compu_method_ref, "CompuMethod")
            if serialized is not None:
                wrapped = ET.Element("COMPU-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize data_constr_ref
        if self.data_constr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_constr_ref, "DataConstr")
            if serialized is not None:
                wrapped = ET.Element("DATA-CONSTR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize display_format
        if self.display_format is not None:
            serialized = SerializationHelper.serialize_item(self.display_format, "DisplayFormatString")
            if serialized is not None:
                wrapped = ET.Element("DISPLAY-FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize display_presentation
        if self.display_presentation is not None:
            serialized = SerializationHelper.serialize_item(self.display_presentation, "DisplayPresentationEnum")
            if serialized is not None:
                wrapped = ET.Element("DISPLAY-PRESENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize implementation_data_type_ref
        if self.implementation_data_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_data_type_ref, "AbstractImplementationDataType")
            if serialized is not None:
                wrapped = ET.Element("IMPLEMENTATION-DATA-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize invalid_value
        if self.invalid_value is not None:
            serialized = SerializationHelper.serialize_item(self.invalid_value, "ValueSpecification")
            if serialized is not None:
                wrapped = ET.Element("INVALID-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize step_size
        if self.step_size is not None:
            serialized = SerializationHelper.serialize_item(self.step_size, "Float")
            if serialized is not None:
                wrapped = ET.Element("STEP-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_addr_method_ref
        if self.sw_addr_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_addr_method_ref, "SwAddrMethod")
            if serialized is not None:
                wrapped = ET.Element("SW-ADDR-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_alignment
        if self.sw_alignment is not None:
            serialized = SerializationHelper.serialize_item(self.sw_alignment, "AlignmentType")
            if serialized is not None:
                wrapped = ET.Element("SW-ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_bit_representation
        if self.sw_bit_representation is not None:
            serialized = SerializationHelper.serialize_item(self.sw_bit_representation, "SwBitRepresentation")
            if serialized is not None:
                wrapped = ET.Element("SW-BIT-REPRESENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_calibration_access
        if self.sw_calibration_access is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calibration_access, "SwCalibrationAccessEnum")
            if serialized is not None:
                wrapped = ET.Element("SW-CALIBRATION-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_calprm_axis_set
        if self.sw_calprm_axis_set is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calprm_axis_set, "SwCalprmAxisSet")
            if serialized is not None:
                wrapped = ET.Element("SW-CALPRM-AXIS-SET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_comparison_variables (list from container "SW-COMPARISON-VARIABLES")
        if self.sw_comparison_variables:
            container = ET.Element("SW-COMPARISON-VARIABLES")
            for item in self.sw_comparison_variables:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("SwVariableRefProxy", package_data):
                    # Simple primitive type
                    child = ET.Element("SW-COMPARISON-VARIABLE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("SwVariableRefProxy", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize sw_data_dependency
        if self.sw_data_dependency is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_dependency, "SwDataDependency")
            if serialized is not None:
                wrapped = ET.Element("SW-DATA-DEPENDENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_host_variable
        if self.sw_host_variable is not None:
            serialized = SerializationHelper.serialize_item(self.sw_host_variable, "SwVariableRefProxy")
            if serialized is not None:
                wrapped = ET.Element("SW-HOST-VARIABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_impl_policy_enum
        if self.sw_impl_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.sw_impl_policy_enum, "SwImplPolicyEnum")
            if serialized is not None:
                wrapped = ET.Element("SW-IMPL-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_intended_resolution
        if self.sw_intended_resolution is not None:
            serialized = SerializationHelper.serialize_item(self.sw_intended_resolution, "Numerical")
            if serialized is not None:
                wrapped = ET.Element("SW-INTENDED-RESOLUTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_interpolation_method
        if self.sw_interpolation_method is not None:
            serialized = SerializationHelper.serialize_item(self.sw_interpolation_method, "Identifier")
            if serialized is not None:
                wrapped = ET.Element("SW-INTERPOLATION-METHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_is_virtual
        if self.sw_is_virtual is not None:
            serialized = SerializationHelper.serialize_item(self.sw_is_virtual, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("SW-IS-VIRTUAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_pointer_target_props
        if self.sw_pointer_target_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_pointer_target_props, "SwPointerTargetProps")
            if serialized is not None:
                wrapped = ET.Element("SW-POINTER-TARGET-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_record_layout_ref
        if self.sw_record_layout_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_ref, "SwRecordLayout")
            if serialized is not None:
                wrapped = ET.Element("SW-RECORD-LAYOUT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_refresh_timing
        if self.sw_refresh_timing is not None:
            serialized = SerializationHelper.serialize_item(self.sw_refresh_timing, "MultidimensionalTime")
            if serialized is not None:
                wrapped = ET.Element("SW-REFRESH-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_text_props
        if self.sw_text_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_text_props, "SwTextProps")
            if serialized is not None:
                wrapped = ET.Element("SW-TEXT-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_value_block_size
        if self.sw_value_block_size is not None:
            serialized = SerializationHelper.serialize_item(self.sw_value_block_size, "Numerical")
            if serialized is not None:
                wrapped = ET.Element("SW-VALUE-BLOCK-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sw_value_block_size_mults (list from container "SW-VALUE-BLOCK-SIZE-MULTS")
        if self.sw_value_block_size_mults:
            container = ET.Element("SW-VALUE-BLOCK-SIZE-MULTS")
            for item in self.sw_value_block_size_mults:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("Numerical", package_data):
                    # Simple primitive type
                    child = ET.Element("SW-VALUE-BLOCK-SIZE-MULT")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("Numerical", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize value_axis_data_type_ref
        if self.value_axis_data_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.value_axis_data_type_ref, "ApplicationPrimitiveDataType")
            if serialized is not None:
                wrapped = ET.Element("VALUE-AXIS-DATA-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "SwDataDefProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDefProps":
        """Deserialize XML element to SwDataDefProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDefProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwDataDefProps, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "SwDataDefProps")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse additional_native_type_qualifier
        child = SerializationHelper.find_child_element(inner_elem, "ADDITIONAL-NATIVE-TYPE-QUALIFIER")
        if child is not None:
            additional_native_type_qualifier_value = child.text
            obj.additional_native_type_qualifier = additional_native_type_qualifier_value

        # Parse annotations (list from container "ANNOTATIONS")
        obj.annotations = []
        container = SerializationHelper.find_child_element(inner_elem, "ANNOTATIONS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("Annotation", package_data):
                    child_value = child.text
                elif is_enum_type("Annotation", package_data):
                    child_value = Annotation.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.annotations.append(child_value)

        # Parse base_type_ref
        child = SerializationHelper.find_child_element(inner_elem, "BASE-TYPE-REF")
        if child is not None:
            base_type_ref_value = ARRef.deserialize(child)
            obj.base_type_ref = base_type_ref_value

        # Parse compu_method_ref
        child = SerializationHelper.find_child_element(inner_elem, "COMPU-METHOD-REF")
        if child is not None:
            compu_method_ref_value = ARRef.deserialize(child)
            obj.compu_method_ref = compu_method_ref_value

        # Parse data_constr_ref
        child = SerializationHelper.find_child_element(inner_elem, "DATA-CONSTR-REF")
        if child is not None:
            data_constr_ref_value = ARRef.deserialize(child)
            obj.data_constr_ref = data_constr_ref_value

        # Parse display_format
        child = SerializationHelper.find_child_element(inner_elem, "DISPLAY-FORMAT")
        if child is not None:
            display_format_value = child.text
            obj.display_format = display_format_value

        # Parse display_presentation
        child = SerializationHelper.find_child_element(inner_elem, "DISPLAY-PRESENTATION")
        if child is not None:
            display_presentation_value = DisplayPresentationEnum.deserialize(child)
            obj.display_presentation = display_presentation_value

        # Parse implementation_data_type_ref
        child = SerializationHelper.find_child_element(inner_elem, "IMPLEMENTATION-DATA-TYPE-REF")
        if child is not None:
            implementation_data_type_ref_value = ARRef.deserialize(child)
            obj.implementation_data_type_ref = implementation_data_type_ref_value

        # Parse invalid_value
        child = SerializationHelper.find_child_element(inner_elem, "INVALID-VALUE")
        if child is not None:
            invalid_value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.invalid_value = invalid_value_value

        # Parse step_size
        child = SerializationHelper.find_child_element(inner_elem, "STEP-SIZE")
        if child is not None:
            step_size_value = child.text
            obj.step_size = step_size_value

        # Parse sw_addr_method_ref
        child = SerializationHelper.find_child_element(inner_elem, "SW-ADDR-METHOD-REF")
        if child is not None:
            sw_addr_method_ref_value = ARRef.deserialize(child)
            obj.sw_addr_method_ref = sw_addr_method_ref_value

        # Parse sw_alignment
        child = SerializationHelper.find_child_element(inner_elem, "SW-ALIGNMENT")
        if child is not None:
            sw_alignment_value = child.text
            obj.sw_alignment = sw_alignment_value

        # Parse sw_bit_representation
        child = SerializationHelper.find_child_element(inner_elem, "SW-BIT-REPRESENTATION")
        if child is not None:
            sw_bit_representation_value = SerializationHelper.deserialize_by_tag(child, "SwBitRepresentation")
            obj.sw_bit_representation = sw_bit_representation_value

        # Parse sw_calibration_access
        child = SerializationHelper.find_child_element(inner_elem, "SW-CALIBRATION-ACCESS")
        if child is not None:
            sw_calibration_access_value = SwCalibrationAccessEnum.deserialize(child)
            obj.sw_calibration_access = sw_calibration_access_value

        # Parse sw_calprm_axis_set
        child = SerializationHelper.find_child_element(inner_elem, "SW-CALPRM-AXIS-SET")
        if child is not None:
            sw_calprm_axis_set_value = SerializationHelper.deserialize_by_tag(child, "SwCalprmAxisSet")
            obj.sw_calprm_axis_set = sw_calprm_axis_set_value

        # Parse sw_comparison_variables (list from container "SW-COMPARISON-VARIABLES")
        obj.sw_comparison_variables = []
        container = SerializationHelper.find_child_element(inner_elem, "SW-COMPARISON-VARIABLES")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("SwVariableRefProxy", package_data):
                    child_value = child.text
                elif is_enum_type("SwVariableRefProxy", package_data):
                    child_value = SwVariableRefProxy.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_comparison_variables.append(child_value)

        # Parse sw_data_dependency
        child = SerializationHelper.find_child_element(inner_elem, "SW-DATA-DEPENDENCY")
        if child is not None:
            sw_data_dependency_value = SerializationHelper.deserialize_by_tag(child, "SwDataDependency")
            obj.sw_data_dependency = sw_data_dependency_value

        # Parse sw_host_variable
        child = SerializationHelper.find_child_element(inner_elem, "SW-HOST-VARIABLE")
        if child is not None:
            sw_host_variable_value = SerializationHelper.deserialize_by_tag(child, "SwVariableRefProxy")
            obj.sw_host_variable = sw_host_variable_value

        # Parse sw_impl_policy_enum
        child = SerializationHelper.find_child_element(inner_elem, "SW-IMPL-POLICY-ENUM")
        if child is not None:
            sw_impl_policy_enum_value = SwImplPolicyEnum.deserialize(child)
            obj.sw_impl_policy_enum = sw_impl_policy_enum_value

        # Parse sw_intended_resolution
        child = SerializationHelper.find_child_element(inner_elem, "SW-INTENDED-RESOLUTION")
        if child is not None:
            sw_intended_resolution_value = child.text
            obj.sw_intended_resolution = sw_intended_resolution_value

        # Parse sw_interpolation_method
        child = SerializationHelper.find_child_element(inner_elem, "SW-INTERPOLATION-METHOD")
        if child is not None:
            sw_interpolation_method_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.sw_interpolation_method = sw_interpolation_method_value

        # Parse sw_is_virtual
        child = SerializationHelper.find_child_element(inner_elem, "SW-IS-VIRTUAL")
        if child is not None:
            sw_is_virtual_value = child.text
            obj.sw_is_virtual = sw_is_virtual_value

        # Parse sw_pointer_target_props
        child = SerializationHelper.find_child_element(inner_elem, "SW-POINTER-TARGET-PROPS")
        if child is not None:
            sw_pointer_target_props_value = SerializationHelper.deserialize_by_tag(child, "SwPointerTargetProps")
            obj.sw_pointer_target_props = sw_pointer_target_props_value

        # Parse sw_record_layout_ref
        child = SerializationHelper.find_child_element(inner_elem, "SW-RECORD-LAYOUT-REF")
        if child is not None:
            sw_record_layout_ref_value = ARRef.deserialize(child)
            obj.sw_record_layout_ref = sw_record_layout_ref_value

        # Parse sw_refresh_timing
        child = SerializationHelper.find_child_element(inner_elem, "SW-REFRESH-TIMING")
        if child is not None:
            sw_refresh_timing_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.sw_refresh_timing = sw_refresh_timing_value

        # Parse sw_text_props
        child = SerializationHelper.find_child_element(inner_elem, "SW-TEXT-PROPS")
        if child is not None:
            sw_text_props_value = SerializationHelper.deserialize_by_tag(child, "SwTextProps")
            obj.sw_text_props = sw_text_props_value

        # Parse sw_value_block_size
        child = SerializationHelper.find_child_element(inner_elem, "SW-VALUE-BLOCK-SIZE")
        if child is not None:
            sw_value_block_size_value = child.text
            obj.sw_value_block_size = sw_value_block_size_value

        # Parse sw_value_block_size_mults (list from container "SW-VALUE-BLOCK-SIZE-MULTS")
        obj.sw_value_block_size_mults = []
        container = SerializationHelper.find_child_element(inner_elem, "SW-VALUE-BLOCK-SIZE-MULTS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("Numerical", package_data):
                    child_value = child.text
                elif is_enum_type("Numerical", package_data):
                    child_value = Numerical.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_value_block_size_mults.append(child_value)

        # Parse unit_ref
        child = SerializationHelper.find_child_element(inner_elem, "UNIT-REF")
        if child is not None:
            unit_ref_value = ARRef.deserialize(child)
            obj.unit_ref = unit_ref_value

        # Parse value_axis_data_type_ref
        child = SerializationHelper.find_child_element(inner_elem, "VALUE-AXIS-DATA-TYPE-REF")
        if child is not None:
            value_axis_data_type_ref_value = ARRef.deserialize(child)
            obj.value_axis_data_type_ref = value_axis_data_type_ref_value

        return obj



class SwDataDefPropsBuilder(BuilderBase):
    """Builder for SwDataDefProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwDataDefProps = SwDataDefProps()


    def with_additional_native_type_qualifier(self, value: Optional[NativeDeclarationString]) -> "SwDataDefPropsBuilder":
        """Set additional_native_type_qualifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.additional_native_type_qualifier = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "SwDataDefPropsBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_base_type(self, value: Optional[SwBaseType]) -> "SwDataDefPropsBuilder":
        """Set base_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_type = value
        return self

    def with_compu_method(self, value: Optional[CompuMethod]) -> "SwDataDefPropsBuilder":
        """Set compu_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.compu_method = value
        return self

    def with_data_constr(self, value: Optional[DataConstr]) -> "SwDataDefPropsBuilder":
        """Set data_constr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_constr = value
        return self

    def with_display_format(self, value: Optional[DisplayFormatString]) -> "SwDataDefPropsBuilder":
        """Set display_format attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.display_format = value
        return self

    def with_display_presentation(self, value: Optional[DisplayPresentationEnum]) -> "SwDataDefPropsBuilder":
        """Set display_presentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.display_presentation = value
        return self

    def with_implementation_data_type(self, value: Optional[AbstractImplementationDataType]) -> "SwDataDefPropsBuilder":
        """Set implementation_data_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation_data_type = value
        return self

    def with_invalid_value(self, value: Optional[ValueSpecification]) -> "SwDataDefPropsBuilder":
        """Set invalid_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.invalid_value = value
        return self

    def with_step_size(self, value: Optional[Float]) -> "SwDataDefPropsBuilder":
        """Set step_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.step_size = value
        return self

    def with_sw_addr_method(self, value: Optional[SwAddrMethod]) -> "SwDataDefPropsBuilder":
        """Set sw_addr_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_addr_method = value
        return self

    def with_sw_alignment(self, value: Optional[AlignmentType]) -> "SwDataDefPropsBuilder":
        """Set sw_alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_alignment = value
        return self

    def with_sw_bit_representation(self, value: Optional[SwBitRepresentation]) -> "SwDataDefPropsBuilder":
        """Set sw_bit_representation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_bit_representation = value
        return self

    def with_sw_calibration_access(self, value: Optional[SwCalibrationAccessEnum]) -> "SwDataDefPropsBuilder":
        """Set sw_calibration_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calibration_access = value
        return self

    def with_sw_calprm_axis_set(self, value: Optional[SwCalprmAxisSet]) -> "SwDataDefPropsBuilder":
        """Set sw_calprm_axis_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calprm_axis_set = value
        return self

    def with_sw_comparison_variables(self, items: list[SwVariableRefProxy]) -> "SwDataDefPropsBuilder":
        """Set sw_comparison_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_comparison_variables = list(items) if items else []
        return self

    def with_sw_data_dependency(self, value: Optional[SwDataDependency]) -> "SwDataDefPropsBuilder":
        """Set sw_data_dependency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_dependency = value
        return self

    def with_sw_host_variable(self, value: Optional[SwVariableRefProxy]) -> "SwDataDefPropsBuilder":
        """Set sw_host_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_host_variable = value
        return self

    def with_sw_impl_policy_enum(self, value: Optional[SwImplPolicyEnum]) -> "SwDataDefPropsBuilder":
        """Set sw_impl_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_impl_policy_enum = value
        return self

    def with_sw_intended_resolution(self, value: Optional[Numerical]) -> "SwDataDefPropsBuilder":
        """Set sw_intended_resolution attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_intended_resolution = value
        return self

    def with_sw_interpolation_method(self, value: Optional[Identifier]) -> "SwDataDefPropsBuilder":
        """Set sw_interpolation_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_interpolation_method = value
        return self

    def with_sw_is_virtual(self, value: Optional[Boolean]) -> "SwDataDefPropsBuilder":
        """Set sw_is_virtual attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_is_virtual = value
        return self

    def with_sw_pointer_target_props(self, value: Optional[SwPointerTargetProps]) -> "SwDataDefPropsBuilder":
        """Set sw_pointer_target_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_pointer_target_props = value
        return self

    def with_sw_record_layout(self, value: Optional[SwRecordLayout]) -> "SwDataDefPropsBuilder":
        """Set sw_record_layout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout = value
        return self

    def with_sw_refresh_timing(self, value: Optional[MultidimensionalTime]) -> "SwDataDefPropsBuilder":
        """Set sw_refresh_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_refresh_timing = value
        return self

    def with_sw_text_props(self, value: Optional[SwTextProps]) -> "SwDataDefPropsBuilder":
        """Set sw_text_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_text_props = value
        return self

    def with_sw_value_block_size(self, value: Optional[Numerical]) -> "SwDataDefPropsBuilder":
        """Set sw_value_block_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_value_block_size = value
        return self

    def with_sw_value_block_size_mults(self, items: list[Numerical]) -> "SwDataDefPropsBuilder":
        """Set sw_value_block_size_mults list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_value_block_size_mults = list(items) if items else []
        return self

    def with_unit(self, value: Optional[Unit]) -> "SwDataDefPropsBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self

    def with_value_axis_data_type(self, value: Optional[ApplicationPrimitiveDataType]) -> "SwDataDefPropsBuilder":
        """Set value_axis_data_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value_axis_data_type = value
        return self


    def add_annotation(self, item: Annotation) -> "SwDataDefPropsBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "SwDataDefPropsBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_sw_comparison_variable(self, item: SwVariableRefProxy) -> "SwDataDefPropsBuilder":
        """Add a single item to sw_comparison_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_comparison_variables.append(item)
        return self

    def clear_sw_comparison_variables(self) -> "SwDataDefPropsBuilder":
        """Clear all items from sw_comparison_variables list.

        Returns:
            self for method chaining
        """
        self._obj.sw_comparison_variables = []
        return self

    def add_sw_value_block_size_mult(self, item: Numerical) -> "SwDataDefPropsBuilder":
        """Add a single item to sw_value_block_size_mults list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_value_block_size_mults.append(item)
        return self

    def clear_sw_value_block_size_mults(self) -> "SwDataDefPropsBuilder":
        """Clear all items from sw_value_block_size_mults list.

        Returns:
            self for method chaining
        """
        self._obj.sw_value_block_size_mults = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SwDataDefProps:
        """Build and return the SwDataDefProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj