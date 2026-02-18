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
from typing import TYPE_CHECKING, Optional, get_type_hints
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
from armodel.serialization.name_converter import NameConverter

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
    """AUTOSAR SwDataDefProps.

    Manually maintained class to handle SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL
    wrapper structure in AUTOSAR XML files.
    """

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

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize SwDataDefProps to XML element.

        AUTOSAR schema uses nested structure: SW-DATA-DEF-PROPS contains
        SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this SwDataDefProps
        """
        # Get XML tag name
        tag = NameConverter.to_xml_tag(self.__class__.__name__)
        elem = ET.Element(tag)

        # Add namespace if provided
        if namespace:
            elem.set("xmlns", namespace)

        # Create SW-DATA-DEF-PROPS-VARIANTS wrapper
        variants_elem = ET.Element("SW-DATA-DEF-PROPS-VARIANTS")

        # Create SW-DATA-DEF-PROPS-CONDITIONAL wrapper
        conditional_elem = ET.Element("SW-DATA-DEF-PROPS-CONDITIONAL")

        # Serialize reference attributes that go inside SW-DATA-DEF-PROPS-CONDITIONAL
        # These are the attributes that are typically references wrapped in -REF elements
        if self.base_type:
            ref_elem = ET.Element("BASE-TYPE-REF")
            ref_elem.set("DEST", "SW-BASE-TYPE")
            ref_elem.text = str(self.base_type) if hasattr(self.base_type, '__str__') else str(self.base_type)
            conditional_elem.append(ref_elem)

        if self.implementation_data_type:
            ref_elem = ET.Element("IMPLEMENTATION-DATA-TYPE-REF")
            ref_elem.set("DEST", "IMPLEMENTATION-DATA-TYPE")
            ref_elem.text = str(self.implementation_data_type) if hasattr(self.implementation_data_type, '__str__') else str(self.implementation_data_type)
            conditional_elem.append(ref_elem)

        if self.data_constr:
            ref_elem = ET.Element("DATA-CONSTR-REF")
            ref_elem.set("DEST", "DATA-CONSTR")
            ref_elem.text = str(self.data_constr) if hasattr(self.data_constr, '__str__') else str(self.data_constr)
            conditional_elem.append(ref_elem)

        if self.compu_method:
            ref_elem = ET.Element("COMPU-METHOD-REF")
            ref_elem.set("DEST", "COMPU-METHOD")
            ref_elem.text = str(self.compu_method) if hasattr(self.compu_method, '__str__') else str(self.compu_method)
            conditional_elem.append(ref_elem)

        if self.unit:
            ref_elem = ET.Element("UNIT-REF")
            ref_elem.set("DEST", "UNIT")
            ref_elem.text = str(self.unit) if hasattr(self.unit, '__str__') else str(self.unit)
            conditional_elem.append(ref_elem)

        # Add conditional to variants
        variants_elem.append(conditional_elem)

        # Add variants to main element
        elem.append(variants_elem)

        # Serialize other attributes using reflection-based approach
        for name, value in vars(self).items():
            # Skip private attributes and already handled ones
            if name.startswith('_') or name in ['base_type', 'implementation_data_type', 'data_constr', 'compu_method', 'unit']:
                continue

            # Skip None values
            if value is None:
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(name)

            # Check if this should be an XML attribute
            if ARObject._is_xml_attribute_static(self.__class__, name):
                elem.set(xml_tag, str(value))
            elif hasattr(value, 'serialize'):
                # Recursively serialize child objects
                child = value.serialize(namespace)
                elem.append(child)
            elif isinstance(value, list):
                # Serialize list items
                wrapper = ET.Element(xml_tag)
                for item in value:
                    if hasattr(item, 'serialize'):
                        wrapper.append(item.serialize(namespace))
                    else:
                        child = ET.Element(xml_tag)
                        child.text = str(item)
                        wrapper.append(child)
                elem.append(wrapper)
            else:
                # Primitive value
                child = ET.Element(xml_tag)
                child.text = str(value)
                elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDefProps":
        """Deserialize XML element to SwDataDefProps.

        AUTOSAR schema uses nested structure: SW-DATA-DEF-PROPS contains
        SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL wrapper.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDefProps instance
        """
        # Create instance without calling __init__
        obj = cls.__new__(cls)

        # Call __init__ to set default values
        obj.__init__()

        # Get type hints to know what attributes to expect
        try:
            type_hints = get_type_hints(cls)
        except Exception:
            # Fallback: Use __annotations__ directly
            type_hints = {}
            for base_cls in cls.__mro__:
                if hasattr(base_cls, '__annotations__'):
                    for attr_name, attr_type_str in base_cls.__annotations__.items():
                        if attr_name not in type_hints:
                            type_hints[attr_name] = attr_type_str

        # Helper function to strip namespace from tag
        def strip_namespace(tag: str) -> str:
            if '}' in tag:
                return tag.split('}')[1]
            return tag

        # Find SW-DATA-DEF-PROPS-VARIANTS element
        variants_elem = None
        for child in element:
            child_tag = strip_namespace(child.tag)
            if child_tag == "SW-DATA-DEF-PROPS-VARIANTS":
                variants_elem = child
                break

        # Find SW-DATA-DEF-PROPS-CONDITIONAL element
        conditional_elem = None
        if variants_elem is not None:
            for child in variants_elem:
                child_tag = strip_namespace(child.tag)
                if child_tag == "SW-DATA-DEF-PROPS-CONDITIONAL":
                    conditional_elem = child
                    break

        # Process reference elements inside SW-DATA-DEF-PROPS-CONDITIONAL
        if conditional_elem is not None:
            for child in conditional_elem:
                child_tag = strip_namespace(child.tag)
                if child_tag == "BASE-TYPE-REF":
                    obj.base_type = child.text
                elif child_tag == "IMPLEMENTATION-DATA-TYPE-REF":
                    obj.implementation_data_type = child.text
                elif child_tag == "DATA-CONSTR-REF":
                    obj.data_constr = child.text
                elif child_tag == "COMPU-METHOD-REF":
                    obj.compu_method = child.text
                elif child_tag == "UNIT-REF":
                    obj.unit = child.text

        # Process other attributes using standard reflection-based approach
        for attr_name, attr_type in type_hints.items():
            # Skip already handled attributes
            if attr_name in ['base_type', 'implementation_data_type', 'data_constr', 'compu_method', 'unit']:
                continue

            # Convert Python name to XML tag
            xml_tag = NameConverter.to_xml_tag(attr_name)

            # Check if this should be an XML attribute
            if ARObject._is_xml_attribute_static(cls, attr_name):
                value = element.get(xml_tag)
            else:
                # Find child element
                child = element.find(xml_tag)
                if child is None:
                    # Try to find by matching stripped tag names
                    for elem in element:
                        if strip_namespace(elem.tag) == xml_tag:
                            child = elem
                            break

                if child is not None:
                    # Get value based on type
                    value = ARObject._extract_value(child, attr_type)
                else:
                    value = None

            # Set attribute
            setattr(obj, attr_name, value)

        return obj


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
